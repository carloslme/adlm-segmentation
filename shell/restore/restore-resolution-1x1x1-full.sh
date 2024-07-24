if [ -d "./segmentation/Inf34/nativeres_250/logs/" ]; then
    echo "$(date +"%Y-%m-%d %H:%M:%S") | Directory ./segmentation/Inf34/nativeres_250/logs/ already exists, skipping creation."
else
    # Attempt to create the directory
    mkdir -p ./segmentation/Inf34/nativeres_250/logs/
    echo "$(date +"%Y-%m-%d %H:%M:%S") | ./segmentation/Inf34/nativeres_250/logs/ directory created"
fi

# load python module
. "./segmentation/prep-env/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/prep-env

# change directory to the script directory
cd ./segmentation/dataset-spider

echo "$(date +"%Y-%m-%d %H:%M:%S") | Restoring started." >> "./segmentation/Inf34/nativeres_250/logs/restoring_1x1x1.log" 2>&1
python restore-native-nii-full.py \
    --restore_type "native" \
    --csv_file ./segmentation/dataset-spider/nnUNet_raw/Dataset034_SPIDER/rescale_info_111.csv \
    --file_ids "['0222', '0224', '0223', '0226', '0225', '0228', '0227', '0231', '0229', '0232', '0236', '0234', '0239', '0237', '0242', '0241', '0244', '0243', '0249', '0245', '0251', '0250', '0253', '0252', '0255', '0254', '0257', '0256']" \
    --output_dir ./segmentation/Inf34/nativeres_250 \
    --input_dir ./segmentation/Inf34/modelres_250 \
    --metadata_file ./segmentation/Inf34/nativeres_250/results_1x1x1.csv >> "./segmentation/Inf34/nativeres_250/logs/restoring_1x1x1.log" 2>&1

# After running the script, check the output and error files in the logs directory. 

echo "$(date +"%Y-%m-%d %H:%M:%S") | File ./segmentation/Inf34/nativeres_250/results_1x1x1 created." >> "./segmentation/Inf34/nativeres_250/logs/restoring_1x1x1.log" 2>&1