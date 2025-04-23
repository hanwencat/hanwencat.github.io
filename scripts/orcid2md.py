import requests
import os
import re

def slugify(text):
    """Generate a URL-friendly slug by removing non-alphanumeric characters and lowercasing."""
    return re.sub(r'\W+', '-', text.lower()).strip('-')

def fetch_publications_from_orcid(orcid_id):
    """
    Fetch the list of works from the ORCID public API.
    Returns the JSON "group" array.
    """
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json().get("group", [])

def extract_orcid_summary_metadata(work_group):
    """
    Extract the first work-summary from an ORCID work_group, including DOI if present.
    Returns a dict with title, date, slug, and doi, or None if no summary exists.
    """
    summaries = work_group.get("work-summary", [])
    if not summaries:
        return None
    s = summaries[0]
    title = (s.get("title") or {}).get("title", {}).get("value") or "No Title"

    # Handle missing publication-date gracefully
    pub_date = s.get("publication-date") or {}
    year  = (pub_date.get("year")  or {}).get("value") or "1900"
    month = (pub_date.get("month") or {}).get("value") or "01"
    day   = (pub_date.get("day")   or {}).get("value") or "01"
    date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    # Attempt to retrieve DOI from external IDs
    doi = None
    ids = work_group.get("external-ids", {}).get("external-id", [])
    for eid in ids:
        if eid.get("external-id-type", "").upper() == "DOI":
            doi = eid.get("external-id-value")
            break

    return {
        "title": title,
        "date": date,
        "slug": slugify(title),
        "doi": doi
    }

def fetch_crossref_metadata(doi):
    """
    Retrieve full publication metadata from Crossref API using DOI.
    Returns the 'message' part of the response.
    """
    url = f"https://api.crossref.org/works/{doi}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("message", {})

def format_bibtex(raw: str) -> str:
    """
    Reformat a one-line BibTeX entry into a multi-line, indented style.
    Example input:
      @article{Key, field1={…}, field2={…}, …}
    → Output:
      @article{Key,
          field1 = {…},
          field2 = {…}
      }
    """
    raw = raw.strip()
    # Split off the "@type{key," header from the rest of the fields
    header, rest = raw.split("{", 1)
    body = rest.rsplit("}", 1)[0]  # drop the trailing "}"
    key, fields_blob = body.split(",", 1)

    # Split into individual fields by commas BEFORE field names (lookahead)
    fields = re.split(r",\s*(?=[a-zA-Z]+ *=)", fields_blob)

    lines = []
    # Rebuild header line
    lines.append(f"{header.strip()}{{{key.strip()},")
    # Indent each field and re-add trailing commas
    for field in fields:
        field = field.strip().rstrip(",")
        lines.append(f"    {field},")
    # Remove comma on last field
    if len(lines) > 1:
        lines[-1] = lines[-1].rstrip(",")
    # Close the entry
    lines.append("}")

    return "\n".join(lines)

def save_bibtex(doi: str, counter: int, output_dir="files") -> str:
    """
    Download the one-line BibTeX from Crossref, reformat it nicely,
    save it to files/bibtex{counter}.bib, and return its relative path.
    """
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    headers = {"Accept": "application/x-bibtex"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    raw_bib = resp.text
    pretty_bib = format_bibtex(raw_bib)

    os.makedirs(output_dir, exist_ok=True)
    bibfile = os.path.join(output_dir, f"bibtex{counter}.bib")
    with open(bibfile, "w", encoding="utf-8") as f:
        f.write(pretty_bib)

    return f"/files/bibtex{counter}.bib"

def generate_md_file(meta, counter, output_md_dir="output_md", files_dir="files"):
    """
    Generate a Markdown file in the specified output directory,
    using the combined metadata from ORCID and Crossref.
    """
    os.makedirs(output_md_dir, exist_ok=True)
    filename = f"{meta['date']}-{meta['slug']}.md"
    path = os.path.join(output_md_dir, filename)

    slidesurl = f"/files/paper{counter}.pdf"
    paperurl  = f"https://doi.org/{meta['doi']}" if meta.get("doi") else ""
    bibtexurl = meta.get("biburl", "")

    # Build author list like "Last, F., Last2, F2."
    authors = []
    for author in meta.get("author", []):
        family = author.get("family", "")
        given = author.get("given", "")
        initials = "".join([n[0] for n in given.split() if n])
        authors.append(f"{family}, {initials}.")
    citation = " ".join(authors) + f" ({meta['year']}). “{meta['title']}.” <i>{meta['container-title']}</i>"
    if meta.get("volume"):
        citation += f", {meta['volume']}"
        if meta.get("issue"):
            citation += f"({meta['issue']})"
    if meta.get("page"):
        citation += f":{meta['page']}."
    else:
        citation += "."

    excerpt = (meta.get("abstract") or "Article abstract here.").replace("\n", " ")

    content = f"""---
title: "{meta['title']}"
collection: publications
category: manuscripts
permalink: /publication/{meta['date']}-{meta['slug']}
excerpt: '{excerpt}'
date: {meta['date']}
venue: '{meta.get('container-title','')}'
slidesurl: '{slidesurl}'
paperurl: '{paperurl}'
bibtexurl: '{bibtexurl}'
citation: '{citation}'
---
{excerpt}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {path}")

def main():
    """
    Prompt for an ORCID iD, fetch works, enrich via Crossref, download
    and reformat BibTeX, then emit one Markdown file per publication.
    """
    orcid_id = input("Enter your ORCID ID (e.g. 0000-0002-1825-0097): ").strip()
    groups = fetch_publications_from_orcid(orcid_id)
    if not groups:
        print("⚠️ No works found for this ORCID.")
        return

    # Counter used for naming files (paper1.pdf, bibtex1.bib, etc.)
    for idx, group in enumerate(groups, start=1):
        summary = extract_orcid_summary_metadata(group)
        if not summary or not summary.get("doi"):
            continue  # skip entries without a DOI

        try:
            cr = fetch_crossref_metadata(summary["doi"])
        except Exception as e:
            print(f"❌ Failed to fetch Crossref data for DOI={summary['doi']}: {e}")
            continue

        # Merge data from ORCID summary and Crossref metadata
        meta = {
            "title": summary["title"],
            "date": summary["date"],
            "slug": summary["slug"],
            "doi": summary["doi"],
            "year": summary["date"][:4],
            "container-title": cr.get("container-title", [None])[0] or "",
            "volume": cr.get("volume", ""),
            "issue": cr.get("issue", ""),
            "page": cr.get("page", ""),
            "author": cr.get("author", []),
            "abstract": (cr.get("abstract") or "").replace("<jats:p>", "").replace("</jats:p>", ""),
            "biburl": save_bibtex(summary["doi"], idx)
        }

        generate_md_file(meta, counter=idx)

    print("🎉 All done! Copy the contents of output_md/ into your `_publications/` folder and push along with the files/ directory.")

if __name__ == "__main__":
    main()