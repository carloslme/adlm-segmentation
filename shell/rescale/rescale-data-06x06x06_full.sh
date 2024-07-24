#!/usr/bin/bash
# This script rescales the full dataset to 06x06x06 
#SBATCH -J "Resc 0.6,0.6,0.6"   # job name
#SBATCH --time=0-08:00:00   # walltime Mac runtime
#SBATCH --output=./segmentation/dataset-spider/nnUNet_raw/Dataset037_SPIDER/logs/rescaling_06x06x06_%A.out
#SBATCH --error=./segmentation/dataset-spider/nnUNet_raw/Dataset037_SPIDER/logs/rescaling_06x06x06_%A.err
#SBATCH --mem=16G
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=16   # number of processor cores (i.e. tasks)
#SBATCH --gres=gpu:0  # replace 0 with 1 if gpu needed
#SBATCH --partition=universe # you can check available partitions with "sinfo" command
# """
# PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
# universe*    up   infinite      5    mix apollo,atlas,chameleon,hercules,prometheus
# universe*    up   infinite      2   idle helios,leto
# """

# load python module
. "./segmentation/prep-env/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/prep-env

# change directory to the script directory
cd ./segmentation/dataset-spider

if [ -d "./nnUNet_raw/Dataset037_SPIDER" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset037_SPIDER already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset037_SPIDER
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset037_SPIDER created."
fi

echo "$(date +"%Y-%m-%d %H:%M:%S") | Rescaling started created." >> "./nnUNet_raw/Dataset037_SPIDER/logs/rescaling_06x06x06.log" 2>&1
# # run the script
python ./rescale-nii-spacing.py \
 --input_dir nnUNet_raw/Dataset000_SPIDER \
 --output_dir nnUNet_raw/Dataset037_SPIDER \
 --csv_file nnUNet_raw/Dataset037_SPIDER/rescale_info_060606.csv \
 --voxel_spacing "(0.6,0.6,0.6)"


# After running the script, check the output and error files in the logs directory. 

echo "$(date +"%Y-%m-%d %H:%M:%S") | Creating dataset.json created." >> "./nnUNet_raw/Dataset037_SPIDER/logs/rescaling_06x06x06.log" 2>&1
# Make json file
python ./segmentation/dataset-spider/full-dataset/scripts/make_jsonfile.py \
        --directory ./segmentation/dataset-spider/nnUNet_raw/Dataset037_SPIDER/imagesTr \
        --output_file ./segmentation/dataset-spider/nnUNet_raw/Dataset037_SPIDER/dataset.json

echo "$(date +"%Y-%m-%d %H:%M:%S") | File ./nnUNet_raw/Dataset037_SPIDER/dataset.json created." >> "./nnUNet_raw/Dataset037_SPIDER/logs/rescaling_06x06x06.log" 2>&1