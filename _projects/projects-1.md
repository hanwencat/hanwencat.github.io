---
title: "Algorithm Project"
# title: "Algorithm Development for Myelin Water Imaging"
excerpt: "Several ML and DL based algorithms were developed for a fast, robust and accurate myelin water imaging (MWI) data postprocessing.<br/><img src='/images/projects/same-ecos.jpg' width='580px' style='display:inline-block'>"
collection: projects
---

The algorithm project focuses on accelerating and improving Myelin Water Imaging (MWI) using machine/deep learning, signal modeling, and information theory. The goal is to make MWI faster, more accurate, and robust for clinical and research applications. Below are three key contributions.

---

## 🔸 Fast Myelin Water Fraction Estimation via Neural Network
A deep neural network was developed to estimate the Myelin Water Fraction (MWF) directly from multi-echo GRASE data. Training labels were derived using a regularized non-negative least squares (NNLS) approach with stimulated echo correction. The proposed method achieves whole-brain MWF map generation in under one minute without GPU acceleration.

**Highlights:**
- Voxel-wise MWF maps show strong agreement with NNLS (R² > 0.98, MAE < 0.01)
- Trained model generalizes to spinal cord, MS lesions, and multi-site data
- Compatible with standard CPUs

<!-- ![NN MWF Pipeline](/images/projects/nn_speedup.png )   -->
<img src='/images/projects/nn-speedup.png'>
<br/>
*Fig. 1. NNLS vs. neural network-based MWF estimation.*

---

## 🔸 SAME-ECOS: Data-Driven Multi-Exponential Spectrum Decomposition
SAME-ECOS (Spectrum Analysis for Multiple Exponentials via Experimental Condition Oriented Simulation) introduces a data-driven pipeline that integrates resolution-limit theory with neural network training. Synthetic training data are generated under realistic noise and resolution constraints based on acquisition parameters, enabling more robust T2 spectrum decomposition.

**Highlights:**
- Achieves >15% improvement in cosine similarity and >10% reduction in MAE vs. NNLS
- Capable of modeling more components without sacrificing stability
- Enables voxel-wise decomposition in under 3 minutes

<img src='/images/projects/same-ecos-phantom.png'>
<br/>
*Fig. 2. Digital phantom tests to compare the performance of SAME-ECOS and NNLS.*

---

## 🔸 SLED: Self-Labelled Encoder-Decoder for Data Postprocessing
The SLED method employs an unsupervised encoder-decoder architecture to estimate MWF from multi-echo data. A three-pool model is fit using latent parameters learned from the input signal itself, eliminating the need for externally labeled training data. This framework allows subject-specific adaptation and improves fitting in low SNR conditions.

**Highlights:**
- Fully self-labelled and unsupervised
- Demonstrates improved stability and reduced noise compared to NLLS
- Validated using high-resolution ex-vivo mouse brain data

<img src='/images/projects/sled-structure.png'>
<br/>
*Fig. 3. Encoder-decoder design of the SLED method.*

---

## 📚 Publications

1. Liu et al., Myelin water imaging data analysis in less than one minute, *NeuroImage*, 2020. [Link to publication](/publication/2020-04-01-myelin-water-imaging-data-analysis-in-less-than-one-minute)
2. Liu et al., A data‐driven T2 relaxation analysis approach for myelin water imaging: Spectrum analysis for multiple exponentials via experimental condition oriented simulation (SAME‐ECOS), *Magnetic Resonance in Medicine*, 2022. [Link to publication](/publication/2022-02-01-a-data-driven-t2-relaxation-analysis-approach-for-myelin-water-imaging-spectrum-analysis-for-multiple-exponentials-via-experimental-condition-oriented-simulation-same-ecos)
3. Liu et al., Self-labelled encoder-decoder (SLED) for multi-echo gradient echo-based myelin water imaging, *NeuroImage*, 2022. [Link to publication](/publication/2022-12-01-self-labelled-encoder-decoder-sled-for-multi-echo-gradient-echo-based-myelin-water-imaging)

---

## 💡 Impact

These developments reduce analysis time, enhance model interpretability, and improve robustness to noise, facilitating broader clinical application of MWI techniques in both human and animal studies.