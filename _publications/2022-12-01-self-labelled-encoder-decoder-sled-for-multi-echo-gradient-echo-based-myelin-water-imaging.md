---
title: "Self-labelled encoder-decoder (SLED) for multi-echo gradient echo-based myelin water imaging"
collection: publications
category: manuscripts
permalink: /publication/2022-12-01-self-labelled-encoder-decoder-sled-for-multi-echo-gradient-echo-based-myelin-water-imaging
excerpt: 'Introducing SLED—a self‐labelled encoder‐decoder network for multi‐echo gradient‐echo myelin water imaging—this unsupervised deep‐learning method produces more accurate and stable myelin water fraction maps with lower noise amplification and strong correlation to conventional NLLS fitting in both phantom and high-resolution mouse brain data.'
date: 2022-12-01
venue: 'NeuroImage'
slidesurl: '/files/paper3.pdf'
paperurl: 'https://doi.org/10.1016/j.neuroimage.2022.119717'
bibtexurl: '/files/bibtex3.bib'
citation: 'Liu, H. Grouza, V. Tuznik, M. Siminovitch, KA. Bagheri, H. Peterson, A. Rudko, DA. (2022). “Self-labelled encoder-decoder (SLED) for multi-echo gradient echo-based myelin water imaging.” <i>NeuroImage</i>, 264:119717.'
---
**Purpose:**

Reconstruction of high quality myelin water imaging (MWI) maps is challenging, particularly for data acquired using multi-echo gradient echo (mGRE) sequences. A non-linear least squares fitting (NLLS) approach has often been applied for MWI. However, this approach may produce maps with limited detail and, in some cases, sub-optimal signal to noise ratio (SNR), due to the nature of the voxel-wise fitting. In this study, we developed a novel, unsupervised learning method called self-labelled encoder-decoder (SLED) to improve gradient echo-based MWI data fitting.

**Methods:**

Ultra-high resolution, MWI data was collected from five mouse brains with variable levels of myelination, using a mGRE sequence. Imaging data was acquired using a 7T preclinical MRI system. A self-labelled, encoder-decoder network was implemented in TensorFlow for calculation of myelin water fraction (MWF) based on the mGRE signal decay. A simulated MWI phantom was also created to evaluate the performance of MWF estimation.

**Results:**

Compared to NLLS, SLED demonstrated improved MWF estimation, in terms of both stability and accuracy in phantom tests. In addition, SLED produced less noisy MWF maps from high resolution MR microscopy images of mouse brain tissue. It specifically resulted in lower noise amplification for all mouse genotypes that were imaged and yielded mean MWF values in white matter ROIs that were highly correlated with those derived from standard NLLS fitting. Lastly, SLED also exhibited higher tolerance to low SNR data.

**Conclusion:**

Due to its unsupervised and self-labeling nature, SLED offers a unique alternative to analyze gradient echo-based MWI data, providing accurate and stable MWF estimations.
