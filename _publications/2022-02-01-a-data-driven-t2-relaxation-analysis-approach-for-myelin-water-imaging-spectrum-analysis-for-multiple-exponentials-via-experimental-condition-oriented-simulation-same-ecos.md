---
title: "A data‐driven T2 relaxation analysis approach for myelin water imaging: Spectrum analysis for multiple exponentials via experimental condition oriented simulation (SAME‐ECOS)"
collection: publications
category: manuscripts
permalink: /publication/2022-02-01-a-data-driven-t2-relaxation-analysis-approach-for-myelin-water-imaging-spectrum-analysis-for-multiple-exponentials-via-experimental-condition-oriented-simulation-same-ecos
excerpt: 'Introducing SAME-ECOS—a data-driven spectrum-analysis method combining resolution-limit constraints with neural networks—this approach achieved over 15% higher cosine similarity and more than 10% lower myelin water fraction error than NNLS in simulations, demonstrated clearer separation of myelin water peaks in vivo, and produced whole-brain MWI maps 30× faster (≈3 min) than conventional methods.'
date: 2022-02-01
venue: 'Magnetic Resonance in Medicine'
slidesurl: '/files/first_author/same-ecos.pdf'
paperurl: 'https://doi.org/10.1002/mrm.29000'
bibtexurl: '/files/bibtex/bibtex4.bib'
citation: 'Liu, H. Joseph, TS. Xiang, Q. Tam, R. Kozlowski, P. Li, DKB. MacKay, AL. Kramer, JLK. Laule, C. (2022). “A data‐driven T2 relaxation analysis approach for myelin water imaging: Spectrum analysis for multiple exponentials via experimental condition oriented simulation (SAME‐ECOS).” <i>Magnetic Resonance in Medicine</i>, 87(2):915-931.'
---
**Purpose:**

The decomposition of multi-exponential decay data into a T2 spectrum poses substantial challenges for conventional fitting algorithms, including non-negative least squares (NNLS). Based on a combination of the resolution limit constraint and machine learning neural network algorithm, a data-driven and highly tailorable analysis method named spectrum analysis for multiple exponentials via experimental condition oriented simulation (SAME-ECOS) was proposed.

**Theory and Methods:**

The theory of SAME-ECOS was derived. Then, a paradigm was presented to demonstrate the SAME-ECOS workflow, consisting of a series of calculation, simulation, and model training operations. The performance of the trained SAME-ECOS model was evaluated using simulations and six in vivo brain datasets. The code is available at https://github.com/hanwencat/SAME-ECOS.

**Results:**

Using NNLS as the baseline, SAME-ECOS achieved over 15% higher overall cosine similarity scores in producing the T2 spectrum, and more than 10% lower mean absolute error in calculating the myelin water fraction (MWF), as well as demonstrated better robustness to noise in the simulation tests. Applying to in vivo data, MWF from SAME-ECOS and NNLS was highly correlated among all study participants. However, a distinct separation of the myelin water peak and the intra/extra-cellular water peak was only observed in the mean T2 spectra determined using SAME-ECOS. In terms of data processing speed, SAME-ECOS is approximately 30 times faster than NNLS, achieving a whole-brain analysis in 3 min.

**Conclusion:**

Compared with NNLS, the SAME-ECOS method yields much more reliable T2 spectra in a dramatically shorter time, increasing the feasibility of multi-component T2 decay analysis in clinical settings.
