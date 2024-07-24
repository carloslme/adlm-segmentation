# Rescale Isotropic

In isotropic scaling, the voxels (volume pixels) in the image have equal dimensions in all three directions (x, y, and z).

We will generate the following configurations for the experiment. More can be created by modifying the scripts:

- 1x1x1
- 0.7x0.7x0.7
- 0.6x0.6x0.6
- 2x2x2
- 0.5x0.5x0.5

## Usage

At this point, we might execute the shell scripts without a problem.

- Give the permission to all the scripts:

```bash
chmod +x rescale-data-3x1x1_full.sh
chmod +x rescale-data-21x07x07_full.sh
chmod +x rescale-data-05x00x00_full.sh
```

### 1x1x1

This dataset will have the voxel space of (1,1,1). For convenience, we call this `Dataset034`.

- Access the [rescale-data-1x1x1_full.sh](shell/rescale/rescale-data-1x1x1_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-1x1x1_full.sh && shell/rescale/rescale-data-1x1x1_full.sh
```

### 2x2x2

This dataset will have the voxel space of (2,2,2). For convenience, we call this `Dataset035`.

- Access the [rescale-data-2x2x2_full.sh](shell/rescale/rescale-data-2x2x2_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-2x2x2_full.sh && shell/rescale/rescale-data-2x2x2_full.sh
```

### 05x05x05

This dataset will have the voxel space of (0.5,0.5,0.5). For convenience, we call this `Dataset035`.

- Access the [rescale-data-05x05x05_full.sh](shell/rescale/rescale-data-05x05x05_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-05x05x05_full.sh && shell/rescale/rescale-data-05x05x05_full.sh
```

### 06x06x06

This dataset will have the voxel space of (0.6,0.6,0.6). For convenience, we call this `Dataset037`.

- Access the [rescale-data-06x06x06_full.sh](shell/rescale/rescale-data-06x06x06_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-06x06x06_full.sh && shell/rescale/rescale-data-06x06x06_full.sh
```

### 07x07x07

This dataset will have the voxel space of (0.7,0.7,0.7). For convenience, we call this `Dataset036`.

- Access the [rescale-data-07x07x07_full.sh](shell/rescale/rescale-data-07x07x07_full.sh) script and verify the arguments are correct.

- Run the script

```bash
chmod +x rescale-data-07x07x07_full.sh && shell/rescale/rescale-data-07x07x07_full.sh
```

## Output

After the rescaling, you will have the following datasets in your `nnUNet_raw` directory.

```bash
./segmentation/dataset-spider/nnUNet_raw
Dataset034_SPIDER
Dataset035_SPIDER
Dataset036_SPIDER
Dataset037_SPIDER
Dataset038_SPIDER
```
