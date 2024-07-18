mkdir logs
echo "$(date +"%Y-%m-%d %H:%M:%S") | Initializing setup" >> "./logs/reorientation.log" 2>&1


# load python module
. "./miniconda3/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./miniconda3

# Reorient derivatives
python ./scripts/reorient-nii.py \
    --input_dir ./dataset-spider/derivatives_spider_new \
    --output_dir ./dataset-spider/reoriented/derivatives_spider_reoriented \
    --csv_file reorientation_derivatives_info.csv >> "./logs/reorientation.log" 2>&1

# Reorient rawdata
python ./scripts/reorient-nii.py \
    --input_dir ./dataset-spider/derivatives_spider_new \
    --output_dir ./dataset-spider/reoriented/derivatives_spider_reoriented \
    --csv_file reorientation_derivatives_info.csv >> "./logs/reorientation.log" 2>&1

echo "$(date +"%Y-%m-%d %H:%M:%S") | Setup finished" >> "./logs/reorientation.log" 2>&1