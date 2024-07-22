cd ./segmentation/dataset-spider/full-dataset/
echo "$(date +"%Y-%m-%d %H:%M:%S") | Initializing test dataset creation." >> "./logs/test_data.log" 2>&1
if [ -d "./nnUNet_raw/Dataset000_SPIDER/test" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory test already exists, skipping creation." >> "./logs/test_data.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset000_SPIDER/test >> "./logs/test_data.log" 2>&1
fi


if [ -d "./nnUNet_raw/Dataset000_SPIDER/test/imagesTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory imagesTr already exists, skipping creation." >> "./logs/test_data.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset000_SPIDER/test/imagesTr >> "./logs/test_data.log" 2>&1
fi

if [ -d "./nnUNet_raw/Dataset000_SPIDER/test/labelsTr" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory labelsTr already exists, skipping creation." >> "./logs/test_data.log" 2>&1
else
    # Attempt to create the directory
    mkdir -p ./nnUNet_raw/Dataset000_SPIDER/test/labelsTr >> "./logs/test_data.log" 2>&1
fi

echo "$(date +"%Y-%m-%d %H:%M:%S") | Directories test/imagesTr and test/labelsTr created." >> "./logs/test_data.log" 2>&1

# # Create test directory and move files
python ./segmentation/dataset-spider/full-dataset/scripts/move_test_data.py \
    --imagesTr_dir ./nnUNet_raw/Dataset000_SPIDER/imagesTr \
    --imagesTr_output_dir ./nnUNet_raw/Dataset000_SPIDER/test/imagesTr \
    --labelsTr_dir ./nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp \
    --labelsTr_output_dir ./nnUNet_raw/Dataset000_SPIDER/test/labelsTr \
    --labelsTr_dir_native ./nnUNet_raw/Dataset000_SPIDER/labelsTr \
    --labelsTr_output_dir_native ./nnUNet_raw/Dataset000_SPIDER/test/labelsTr_native \
    --list_files "['0222', '0224', '0223', '0226', '0225', '0228', '0227', '0231', '0229', '0233', '0232', '0236', '0234', '0239', '0237', '0242', '0241', '0244', '0243', '0249', '0245', '0251', '0250', '0253', '0252', '0255', '0254', '0257', '0256']"  >> "./logs/test_data.log" 2>&1


# Deleting 14 labels labelsTr, in test is keept since it is used in evaluation step
rm -r ./nnUNet_raw/Dataset000_SPIDER/labelsTr
echo "$(date +"%Y-%m-%d %H:%M:%S") | labelsTr with 14 labels deleted.." >> "./logs/test_data.log" 2>&1

# Renaming 4 labels labelsTr_tmp to labelsTr
mv ./nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp ./nnUNet_raw/Dataset000_SPIDER/labelsTr
echo "$(date +"%Y-%m-%d %H:%M:%S") | labelsTr_tmp with 4 labels renamed to labelsTr." >> "./logs/test_data.log" 2>&1

echo "$(date +"%Y-%m-%d %H:%M:%S") | Test data moved." >> "./logs/test_data.log" 2>&1