# load python module
. "./segmentation/prep-env/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/prep-env

# change directory to the script directory
cd ./segmentation/dataset-spider

if [ -d "./nnUNet_raw/Dataset033_SPIDER" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset033_SPIDER
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER created."
fi

if [ -d "./nnUNet_raw/Dataset033_SPIDER/imagesTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER/imagesTr already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset033_SPIDER/imagesTr
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER/imagesTr created."
fi

if [ -d "./nnUNet_raw/Dataset033_SPIDER/labelsTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER/labelsTr already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset033_SPIDER/labelsTr
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset033_SPIDER/labelsTr created."
fi

# run the script
python ./rescale-nii-spacing.py \
 --input_dir nnUNet_raw/Dataset000_SPIDER \
 --output_dir nnUNet_raw/Dataset033_SPIDER \
 --csv_file nnUNet_raw/Dataset033_SPIDER/rescale_info_050000.csv \
 --voxel_spacing "(0.5,origin,origin)"


# After running the script, check the output and error files in the logs directory. 

echo "$(date +"%Y-%m-%d %H:%M:%S") | Creating dataset.json created." >> "./segmentation/dataset-spider/nnUNet_raw/Dataset033_SPIDER/logs/make_json.log" 2>&1
# Make json file
python ./segmentation/dataset-spider/full-dataset/scripts/make_jsonfile.py \
        --directory ./segmentation/dataset-spider/nnUNet_raw/Dataset033_SPIDER/imagesTr \
        --output_file ./segmentation/dataset-spider/nnUNet_raw/Dataset033_SPIDER/dataset.json

echo "$(date +"%Y-%m-%d %H:%M:%S") | File ./nnUNet_raw/Dataset033_SPIDER/dataset.json created." >> "./segmentation/dataset-spider/nnUNet_raw/Dataset033_SPIDER/logs/make_json.log" 2>&1