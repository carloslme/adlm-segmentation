if [ -d "./logs" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory logs already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./logs
fi

cd ./dataset-spider/
touch ./logs/full_dataset_conversion.log
echo "$(date +"%Y-%m-%d %H:%M:%S") | Initializing full dataset conversion." >> "./logs/full_dataset_conversion.log" 2>&1

# load python module
. "./miniconda3/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./miniconda3

if [ -d "./nnUNet_raw/Dataset000_SPIDER/imagesTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset000_SPIDER/imagesTr already exists, skipping creation." >> "./logs/full_dataset_conversion.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset000_SPIDER/imagesTr
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset000_SPIDER/imagesTr created." >> "./logs/full_dataset_conversion.log" 2>&1
fi

if [ -d "./nnUNet_raw/Dataset000_SPIDER/labelsTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset000_SPIDER/labelsTr already exists, skipping creation." >> "./logs/full_dataset_conversion.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset000_SPIDER/labelsTr
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory nnUNet_raw/Dataset000_SPIDER/labelsTr created." >> "./logs/full_dataset_conversion.log" 2>&1
fi


# # Create imagesTr and labelsTr directories with the files
python ./scripts/dataset-format.py \
    --full_dataset True \
    --input_dir_imagesTr ./rawdata_normalized_reoriented \
    --output_dir_imagesTr ./nnUNet_raw/Dataset000_SPIDER/imagesTr \
    --input_dir_labelsTr ./derivatives_spider_reoriented \
    --output_dir_labelsTr ./nnUNet_raw/Dataset000_SPIDER/labelsTr \
    --csv_file ./full_dataset_conversion_results.csv >> "./logs/full_dataset_conversion.log" 2>&1

echo "$(date +"%Y-%m-%d %H:%M:%S") | Validating data..." >> "./logs/full_dataset_conversion.log" 2>&1
# # Validating data
python ./scripts/validate_data.py \
    --csv_file ./full_dataset_conversion_results.csv \
    --report_file ./validation_full_dataset.csv >> "./logs/full_dataset_conversion.log" 2>&1

echo "$(date +"%Y-%m-%d %H:%M:%S") | Data validated, please the check the ./validation_full_dataset.csv for details." >> "./logs/full_dataset_conversion.log" 2>&1