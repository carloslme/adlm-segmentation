import os
import json
import nibabel as nib
from nilearn.image import resample_img
from panoptica.metrics.dice import _compute_dice_coefficient
from panoptica.metrics.assd import _average_surface_distance
import TPTBox as tpt
import numpy as np

class NiftiProcessor:
    @staticmethod
    def resample_nifti_to_match(source_img, reference_img):
        resampled_img = resample_img(source_img, target_affine=reference_img.affine, target_shape=reference_img.shape)
        return resampled_img

    @staticmethod
    def load_and_resample(refpath, prepath, label):
        ref_nii = tpt.NII.load(refpath, seg=True)
        pre_nii = tpt.NII.load(prepath, seg=True)
        
        ref_img = nib.load(refpath)
        pre_img = nib.load(prepath)
        voxel_spacing = ref_img.header.get_zooms()
        
        pre_img_resampled = NiftiProcessor.resample_nifti_to_match(pre_img, ref_img)
        
        pre = tpt.NII(pre_img_resampled).extract_label(label).get_seg_array()
        ref = ref_nii.extract_label(label).get_seg_array()
        
        return ref, pre, voxel_spacing

class MetricsEvaluator:
    @staticmethod
    def compute_metrics(ref, pre, voxel_spacing):
        dice_score = _compute_dice_coefficient(ref, pre)
        assd_score = _average_surface_distance(ref, pre, voxelspacing=voxel_spacing)
        return dice_score, assd_score

    @staticmethod
    def remove_outliers(data, threshold=3):
        return [x for x in data if x <= threshold]

class EvaluationPipeline:
    def __init__(self, ref_folders, num_labels):
        self.ref_folders = ref_folders
        self.num_labels = num_labels
        self.scores_dict = self.initialize_scores_dict()

    def initialize_scores_dict(self):
        return {ref: {pred: {label: {'dice': [], 'assd': [], 'files': []} for label in range(1, self.num_labels + 1)} for pred in preds} for ref, preds in self.ref_folders.items()}

    def process(self):
        for ref_folder, pred_folders in self.ref_folders.items():
            ref_files = {f: os.path.join(ref_folder, f) for f in os.listdir(ref_folder) if f.endswith('.nii.gz')}
            for pred_folder in pred_folders:
                pre_files = {f: os.path.join(pred_folder, f) for f in os.listdir(pred_folder) if f.endswith('.nii.gz')}
                print(f"Processing reference folder {ref_folder} with prediction folder {pred_folder}")
                
                for label in range(1, self.num_labels + 1):
                    print(f"  Processing label {label}")
                    for filename in ref_files:
                        if filename in pre_files:
                            refpath = ref_files[filename]
                            prepath = pre_files[filename]
                            try:
                                ref, pre, voxel_spacing = NiftiProcessor.load_and_resample(refpath, prepath, label)
                                dice, assd = MetricsEvaluator.compute_metrics(ref, pre, voxel_spacing)
                                print(f"    {filename}: Dice = {dice}, ASSD = {assd}")
                                self.scores_dict[ref_folder][pred_folder][label]['dice'].append(dice)
                                self.scores_dict[ref_folder][pred_folder][label]['assd'].append(assd)
                                self.scores_dict[ref_folder][pred_folder][label]['files'].append({
                                    'filename': filename,
                                    'dice': dice,
                                    'assd': assd
                                })
                            except ValueError as e:
                                print(f"    Skipping {filename} due to error: {e}")
                        else:
                            print(f"    Prediction file for {filename} not found in {pred_folder}")
        return self.scores_dict

class ResultsAnalyzer:
    def __init__(self, scores_dict):
        self.scores_dict = scores_dict

    def evaluate(self):
        overall_results = {}
        
        for ref_folder, preds in self.scores_dict.items():
            for pred_folder, scores in preds.items():
                total_dice = []
                total_assd = []
                
                print(f"Results for {ref_folder} with {pred_folder}:")
                for label in scores:
                    filtered_assd = MetricsEvaluator.remove_outliers(scores[label]['assd'])
                    avg_dice = np.mean(scores[label]['dice'])
                    std_dice = np.std(scores[label]['dice'])
                    avg_assd = np.mean(filtered_assd)
                    std_assd = np.std(filtered_assd)
                    
                    total_dice.extend(scores[label]['dice'])
                    total_assd.extend(filtered_assd)
                    
                    print(f"  Label {label}: Average Dice = {avg_dice} ± {std_dice}, Average ASSD = {avg_assd} ± {std_assd}")
                
                overall_avg_dice = np.mean(total_dice)
                overall_std_dice = np.std(total_dice)
                overall_avg_assd = np.mean(total_assd)
                overall_std_assd = np.std(total_assd)
                
                overall_results[(ref_folder, pred_folder)] = {
                    'dice': (overall_avg_dice, overall_std_dice),
                    'assd': (overall_avg_assd, overall_std_assd),
                    'details': scores
                }
                
                print(f"  Overall: Average Dice = {overall_avg_dice} ± {overall_std_dice}, Average ASSD = {overall_avg_assd} ± {overall_std_assd}")
        
        return overall_results

class ResultsSaver:
    @staticmethod
    def save_to_json(overall_results, save_path):
        for (ref_folder, pred_folder), metrics in overall_results.items():
            pred_folder_basename = os.path.basename(pred_folder)
            pred_folder_parent = os.path.basename(os.path.dirname(pred_folder))
            filename = f"{pred_folder_parent}_{pred_folder_basename}.json"
            results_dict = {
                'average_dice': metrics['dice'],
                'average_assd': metrics['assd'],
                'details': metrics['details']
            }
            with open(os.path.join(save_path, filename), 'w') as json_file:
                json.dump(results_dict, json_file, indent=4)
            print(f"Results saved to {os.path.join(save_path, filename)}")

if __name__ == "__main__":
    ref_folders = {
        '/vol/aimspace/projects/practical_SoSe24/segmentation/dataset-spider/nnUNet_raw/Dataset020_SPIDER/test/labelsTr': [
           '/vol/aimspace/projects/practical_SoSe24/segmentation/Phil-experiments/Inf39/modelres_250',
        ],
    }

    evaluation_pipeline = EvaluationPipeline(ref_folders, num_labels=3)
    scores_dict = evaluation_pipeline.process()

    results_analyzer = ResultsAnalyzer(scores_dict)
    overall_results = results_analyzer.evaluate()
    
    print("\nOverall results for all folders:")
    for (ref_folder, pred_folder), metrics in overall_results.items():
        print(f"{ref_folder} with {pred_folder}: Overall Average Dice = {metrics['dice'][0]} ± {metrics['dice'][1]}, Overall Average ASSD = {metrics['assd'][0]} ± {metrics['assd'][1]}")

    save_path = '/vol/aimspace/projects/practical_SoSe24/segmentation/Phil-experiments/Evaluation/foodprints'
    ResultsSaver.save_to_json(overall_results, save_path)
