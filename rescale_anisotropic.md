# Rescale Anisotropic

In anisotropic scaling, the spacing between voxels varies between spatial dimensions.

We will generate the following configurations for the experiment. More can be created by modifying the scripts:

- 3x1x1
- 2.1x0.7x0.7
- 0.5x0.0x0.0 (0.0 is origin or native voxel spacing)

## Usage

At this point, we might execute the shell scripts without a problem.

- Give the permission to all the scripts:

```bash
chmod +x rescale-data-3x1x1_full.sh
chmod +x rescale-data-21x07x07_full.sh
chmod +x rescale-data-05x00x00_full.sh
```

### 3x1x1

This dataset will have the voxel space of (3,1,1). For convenience, we call this `Dataset031`.

- Access the [rescale-data-3x1x1_full.sh](shell/rescale/rescale-data-3x1x1_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-3x1x1_full.sh && shell/rescale/rescale-data-3x1x1_full.sh
```

### 21x07x07

This dataset will have the voxel space of (2.1,0.7,0.7). For convenience, we call this `Dataset032`.

- Access the [rescale-data-21x07x07_full.sh](shell/rescale/rescale-data-21x07x07_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-21x07x07_full.sh && shell/rescale/rescale-data-21x07x07_full.sh
```

### 05x00x00

This dataset will have the voxel space of (0.5,native,native). For convenience, we call this `Dataset033`.

- Access the [rescale-data-05x00x00_full.sh](shell/rescale/rescale-data-05x00x00_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-05x00x00_full.sh && shell/rescale/rescale-data-05x00x00_full.sh
```

## Output

After the rescaling, you will have the following datasets in your `nnUNet_raw` directory.

```bash
./segmentation/dataset-spider/nnUNet_raw
Dataset031_SPIDER
Dataset032_SPIDER
Dataset033_SPIDER
```
