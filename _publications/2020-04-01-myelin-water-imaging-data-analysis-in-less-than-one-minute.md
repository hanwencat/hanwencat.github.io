---
title: "Myelin water imaging data analysis in less than one minute"
collection: publications
category: manuscripts
permalink: /publication/2020-04-01-myelin-water-imaging-data-analysis-in-less-than-one-minute
excerpt: 'This study introduces a deep‐learning neural network that generates whole‐brain myelin water fraction (MWF) maps in under one minute—achieving R²>0.98 and mean absolute error <0.01 compared to conventional NNLS methods across multiple brain and spinal cord datasets, all without GPU acceleration.'
date: 2020-04-01
venue: 'NeuroImage'
slidesurl: '/files/first_author/nn_speedup.pdf'
paperurl: 'https://doi.org/10.1016/j.neuroimage.2020.116551'
bibtexurl: '/files/bibtex8.bib'
citation: 'Liu, H. Xiang, Q. Tam, R. Dvorak, AV. MacKay, AL. Kolind, SH. Traboulsee, A. Vavasour, IM. Li, DK. Kramer, JK. Laule, C. (2020). “Myelin water imaging data analysis in less than one minute.” <i>NeuroImage</i>, 210:116551.'
---
**Purpose:**

Based on a deep learning neural network (NN) algorithm, a super fast and easy to implement data analysis method was proposed for myelin water imaging (MWI) to calculate the myelin water fraction (MWF).

**Methods:**

A NN was constructed and trained on MWI data acquired by a 32-echo 3D gradient and spin echo (GRASE) sequence. Ground truth labels were created by regularized non-negative least squares (NNLS) with stimulated echo corrections. Voxel-wise GRASE data from 5 brains (4 healthy, 1 multiple sclerosis (MS)) were used for NN training. The trained NN was tested on 2 healthy brains, 1 MS brain with segmented lesions, 1 healthy spinal cord, and 1 healthy brain acquired from a different scanner.

**Results:**

Production of whole brain MWF maps in approximately 33 ​s can be achieved by a trained NN without graphics card acceleration. For all testing regions, no visual differences between NN and NNLS MWF maps were observed, and no obvious regional biases were found. Quantitatively, all voxels exhibited excellent agreement between NN and NNLS (all R2>0.98, p ​< ​0.001, mean absolute error <0.01).

**Conclusion:**

The time for accurate MWF calculation can be dramatically reduced to less than 1 ​min by the proposed NN, addressing one of the barriers facing future clinical feasibility of MWI.
