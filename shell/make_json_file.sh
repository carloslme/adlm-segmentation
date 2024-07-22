cd ./segmentation/dataset-spider/full-dataset/

echo "$(date +"%Y-%m-%d %H:%M:%S") | Creating dataset.json" >> "./logs/make_json.log" 2>&1

# load python module
. "./segmentation/py39/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/py39

# Make json file
python ./scripts/make_jsonfile.py \
        --directory ./nnUNet_raw/Dataset000_SPIDER/imagesTr \
        --output_file ./nnUNet_raw/Dataset000_SPIDER/dataset.json

echo "$(date +"%Y-%m-%d %H:%M:%S") | File ./nnUNet_raw/Dataset000_SPIDER/dataset.json created." >> "./logs/make_json.log" 2>&1