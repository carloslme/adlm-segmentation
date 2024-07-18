# Master Practical: Segmentation

Repository for the content of the practical course of Applied Deep Learning in Medicine (ADLM).

## Project goal

Evaluate the impact of image resolution on segmentation accuracy with different resolutions generated from the SPIDER dataset (Semantic Segmentation + Instance Segmentation).

![Diagram](imgs/resolutions.png)

## Overview

### Diagram

**TODO** Insert diagram with general overview.

### Dataset

We are using the SPIDER dataset already normalized. The steps to download it are in the next steps.
> Ask Hendrik about this? How to access it? Shall we upload it to Google Drive?

## Prerrequisites

This installation assumes the following preconditions:

- Linux environment (this was developed in Ubuntu 22.04.4 LTS)
- Conda environment (24.1.2)
- Python 3.9

## Project goal

Evaluate the impact of image resolution on segmentation accuracy with different resolutions generated from the SPIDER dataset (Semantic Segmentation + Instance Segmentation).

## Setup

### Setup the environment

Access this [setup file](setup.md) to configure your environment.

### Preprocessing

**Ensure you are working in the `segmentation` directory you created before.**

#### Download normalized dataset

First, let's download the dataset.
> TODO: add instructions to download the dataset, probably from google drive.

* Create a folder and name it `dataset-spider`
* Download the dataset in this directory

#### Merge modalities

In this step, we need to merge the modalities T1w, T2W, and T2w_acq_iso in order to use the full dataset. Ensure your dataset has this structure:
<details>
<summary>Click to see the directory with the raw images structure. It contains the subjects from the three modalities.</summary>

```bash
rawdata_normalized
├── sub-0001
│   ├── T1w
│   │   └── sub-0001_T1w.nii.gz
│   └── T2w
│       └── sub-0001_T2w.nii.gz
├── sub-0002
│   ├── T1w
│   │   └── sub-0002_T1w.nii.gz
│   └── T2w
│       └── sub-0002_T2w.nii.gz
├── sub-0003
│   ├── T1w
│   │   └── sub-0003_T1w.nii.gz
│   └── T2w
│       └── sub-0003_T2w.nii.gz
├── sub-0004
│   ├── T1w
│   │   └── sub-0004_T1w.nii.gz
│   └── T2w
│       └── sub-0004_T2w.nii.gz
├── sub-0005
│   ├── T1w
│   │   └── sub-0005_T1w.nii.gz
│   └── T2w
│       ├── sub-0005_acq-iso_T2w.nii.gz
│       └── sub-0005_T2w.nii.gz
├── sub-0006
│   └── T2w
│       └── sub-0006_T2w.nii.gz
├── sub-0007
│   ├── T1w
│   │   └── sub-0007_T1w.nii.gz
│   └── T2w
│       ├── sub-0007_acq-iso_T2w.nii.gz
│       └── sub-0007_T2w.nii.gz
```

</details>  

#### Reorient the data

We need to reorient the images to a unique orientation, let's do it to RAS (RAS means that the first dimension orients towards ***R***ight, the second dimension orients towards ***A***nterior, the third dimension orients towards ***S***uperior.)

Access this [reorientation.md](reorientation.md) file and follow to instructions to reorient the data.
