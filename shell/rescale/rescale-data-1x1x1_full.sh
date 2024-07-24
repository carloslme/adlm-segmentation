#!/usr/bin/bash
# load python module
. "./segmentation/prep-env/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/prep-env

# change directory to the script directory
cd ./segmentation/dataset-spider

if [ -d "./nnUNet_raw/Dataset034_SPIDER" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset034_SPIDER already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset034_SPIDER
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset034_SPIDER created."
fi

echo "$(date +"%Y-%m-%d %H:%M:%S") | Rescaling started created." >> "./nnUNet_raw/Dataset034_SPIDER/logs/make_json.log" 2>&1
# # run the script
python ./rescale-nii-spacing.py \
 --input_dir nnUNet_raw/Dataset000_SPIDER \
 --output_dir nnUNet_raw/Dataset034_SPIDER \
 --csv_file nnUNet_raw/Dataset034_SPIDER/rescale_info_111.csv \
 --voxel_spacing "(1,1,1)"

echo "$(date +"%Y-%m-%d %H:%M:%S") | Creating dataset.json created." >> "./nnUNet_raw/Dataset034_SPIDER/logs/make_json.log" 2>&1
# Make json file
python ./segmentation/dataset-spider/full-dataset/scripts/make_jsonfile.py \
        --directory ./segmentation/dataset-spider/nnUNet_raw/Dataset034_SPIDER/imagesTr \
        --output_file ./segmentation/dataset-spider/nnUNet_raw/Dataset034_SPIDER/dataset.json

echo "$(date +"%Y-%m-%d %H:%M:%S") | File ./nnUNet_raw/Dataset034_SPIDER/dataset.json created." >> "./nnUNet_raw/Dataset034_SPIDER/logs/make_json.log" 2>&1