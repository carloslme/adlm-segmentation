# load python module
. "./segmentation/py39/etc/profile.d/conda.sh"

# activate corresponding environment
conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/07x07x07/nnUNet_results'

export nnUNet_preprocessed='./segmentation/07x07x07/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset036_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf36/modelres_500 -d 036 -c 3d_fullres -f 0 --save_probabilities 

conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/06x06x06/nnUNet_results'

export nnUNet_preprocessed='./segmentation/06x06x06/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset037_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf37/modelres_500 -d 037 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/1x1x1/nnUNet_results'

export nnUNet_preprocessed='./segmentation/1x1x1/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset034_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf34/modelres_500 -d 034 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/05x05x05/nnUNet_results'

export nnUNet_preprocessed='./segmentation/05x05x05/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset038_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf38/modelres_500 -d 038 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/2x2x2/nnUNet_results'

export nnUNet_preprocessed='./segmentation/2x2x2/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset035_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf35/modelres_500 -d 035 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/05x00x00/nnUNet_results'

export nnUNet_preprocessed='./segmentation/05x00x00/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset033_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf33/modelres_500 -d 033 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/3x1x1/nnUNet_results'

export nnUNet_preprocessed='./segmentation/3x1x1/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset031_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf31/modelres_500 -d 031 -c 3d_fullres -f 0 --save_probabilities 



conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/21x07x07/nnUNet_results'

export nnUNet_preprocessed='./segmentation/21x07x07/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/nnUNet_raw/Dataset032_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf32/modelres_500 -d 032 -c 3d_fullres -f 0 --save_probabilities 


conda deactivate
conda activate ./segmentation/py39

export nnUNet_results='./segmentation/native/nnUNet_results'

export nnUNet_preprocessed='./segmentation/native/nnUNet_preprocessed'

export nnUNet_raw='./segmentation/dataset-spider/nnUNet_raw'

nnUNetv2_predict -i ./segmentation/dataset-spider/full-dataset/nnUNet_raw/Dataset000_SPIDER/test/imagesTr -o ./segmentation/Phil-experiments/Inf39/modelres_250 -d 020 -c 3d_fullres -f 0 --save_probabilities 
