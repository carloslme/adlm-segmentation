# Verify dataset integrity and Training

## Preprocess and train for 1x1x1
### 1. Create directory

Create a folder with the resolution, for example 1x1x1 for resolution (1,1,1)

### 2. Create preprocessing and validation script

- Create a shell script called `1_preprocessing_1x1x1`.
- Copy the following code to start to the data preprocessing script and verify the dataset integrity.

```bash
cd ./segmentation/training/1x1x1

# Check if the directory exists
if [ -d "./logs" ]; then
    echo "Directory logs already exists, skipping creation." >> "./logs/integrity.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./logs
fi

echo "$(date +"%Y-%m-%d %H:%M:%S") | Initializing validation and preprocessing" >> "./logs/integrity.log" 2>&1
mkdir nnUNet_preprocessed
mkdir nnUNet_results


export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'
export nnUNet_preprocessed='./segmentation/training/1x1x1/nnUNet_preprocessed'
export nnUNet_results='./segmentation/training/1x1x1/nnUNet_results'

echo $nnUNet_raw
echo $nnUNet_preprocessed
echo $nnUNet_results

# load python module
. "./segmentation/py39/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/py39

nnUNetv2_plan_and_preprocess -d 034 --verify_dataset_integrity >> "./logs/integrity.log" 2>&1

echo "$(date +"%Y-%m-%d %H:%M:%S") | Validation finished" >> "./logs/integrity.log" 2>&1
```

### 3. Execute preprocessing script

- Change the working directory `cd ./training/1x1x1`
- Give permissions

    ```bash
    chmod +x ./1_preprocessing_1x1x1.sh
    ```

- Run the script

    ```bash
    ./1_preprocessing_1x1x1.sh
    ```

### 4. Train

- Create a shell script named `2_training_250e_3d_1x1x1.sh` for the training and copy the following code.

```bash
#!/usr/bin/bash

#SBATCH -J "Full-1x1x1 250 Epochs 3D"   # job name
#SBATCH --time=0-48:00:00   # walltime Mac runtime
#SBATCH --output=./segmentation/training/1x1x1/logs/train_250e_3d_%A.out 
#SBATCH --error=./segmentation/training/1x1x1/logs/train_250e_3d_%A.err
#SBATCH --mem=32G
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=16   # number of processor cores (i.e. tasks)
#SBATCH --gres=gpu:1  # replace 0 with 1 if gpu needed
#SBATCH --partition=universe # you can check available partitions with "sinfo" command
# """
# PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
# universe*    up   infinite      5    mix apollo,atlas,chameleon,hercules,prometheus
# universe*    up   infinite      2   idle helios,leto
# """

# load python module
. "./segmentation/py39/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/py39

# change directory to the script directory
cd ./segmentation/training/1x1x1

# run the script
export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'
export nnUNet_preprocessed='./segmentation/training/1x1x1/nnUNet_preprocessed'
export nnUNet_results='./segmentation/training/1x1x1/nnUNet_results'

nnUNetv2_train 034 3d_fullres 0 -num_gpus 1 -tr nnUNetTrainer_250epochs

# After running the script, check the output and error files in the logs directory. 
```

- Send the job to the Slurm Workload Manager

```bash
sbatch ./2_training_250e_3d_1x1x1.sh
```

### 5. Results

You can check the results in the `./1x1x1/nnUNet_results` directory.

## How to preprocess and train the other models?

If you need to train the other datasets, repeat the previous steps changing the `1x1x1` by `3x1x1`, or `2x2x2`, etc. Also, ensure the dataset number is correct according to the resolution.

You can find more information in the [model training](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/how_to_use_nnunet.md#model-training) in the official documentation.
