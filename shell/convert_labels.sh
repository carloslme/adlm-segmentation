cd ./dataset-spider/full-dataset
echo "$(date +"%Y-%m-%d %H:%M:%S") | Initializing labels conversion" >> "./logs/labels_conversion.log" 2>&1


# load python module
. "./miniconda3/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./miniconda3

if [ -d "nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp" ]; then
    echo "Directory nnUNet_raw/Dataset000_SPIDER/labelsTr already exists, skipping creation." >> "./logs/labels_conversion.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp >> "./logs/labels_conversion.log" 2>&1
fi

echo "Converting labels." >> "./logs/labels_conversion.log" 2>&1
python scripts/convert_labels.py \
    --source_dir ./nnUNet_raw/Dataset000_SPIDER/labelsTr \
    --target_dir ./nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp \
    --csv_file nnUNet_raw/Dataset000_SPIDER/labels_conversion.csv \
    >> "./logs/labels_conversion.log" 2>&1
echo "Labels converted, please the check the nnUNet_raw/Dataset000_SPIDER/labels_conversion.csv for details." >> "./logs/full_dataset_conversion.log" 2>&1

