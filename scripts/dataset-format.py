import os
import shutil
import argparse
import csv
from tqdm import tqdm


class NUUNetDatasetConverter:
    def __init__(self, input_dir_imagesTr:str, output_dir_imagesTr:str, input_dir_labelsTr:str, output_dir_labelsTr:str, csv_file:str):
        self.input_dir_imagesTr = input_dir_imagesTr
        self.output_dir_imagesTr = output_dir_imagesTr
        self.input_dir_labelsTr = input_dir_labelsTr
        self.output_dir_labelsTr = output_dir_labelsTr
        self.csv_file = csv_file
        self.csv_headers = ["Input File Directory", "Output File Directory"]
        self.csv_data = []

    def create_imagesTr(self, modality: str, include_iso = False):

        # Create the target directory if it doesn't exist
        os.makedirs(self.output_dir_imagesTr, exist_ok=True)

        # Iterate over the subdirectories in the source directory
        for sub in os.listdir(self.input_dir_imagesTr):
            sub_dir = os.path.join(self.input_dir_imagesTr, sub)
            if os.path.isdir(sub_dir):
                # Iterate over the modalities directories
                # for t_dir in [modality, 'modality']:
                for t_dir in [modality]:
                    t_dir_path = os.path.join(sub_dir, t_dir)
                    if os.path.isdir(t_dir_path):
                        # Iterate over the files in the modality directory
                        for file in os.listdir(t_dir_path):
                            if "acq-iso" in file:
                                pass
                            elif not include_iso:
                                if file.endswith('.nii.gz'):
                                    # Construct the new filename and copy the file
                                    new_filename = f'SPIDER_{sub[-4:]}_{"0001"}.nii.gz'
                                    shutil.copy(os.path.join(t_dir_path, file), os.path.join(self.output_dir_imagesTr, new_filename))
                                    
                                    # Append the conversion information to the CSV data
                                    self.csv_data.append([os.path.join(t_dir_path, file), os.path.join(self.output_dir_imagesTr, new_filename)])
        
        print("imagesTr directory transformation completed.")


    def create_labelsTr(self, modality: str):

        # Create the target directory if it does not exist
        os.makedirs(self.output_dir_labelsTr , exist_ok=True)

        # Iterate over the subdirectories in the source directory
        for subdir in os.listdir(self.input_dir_labelsTr):
            # Define the path to the modality directory
            modality_dir = os.path.join(self.input_dir_labelsTr, subdir, modality)

            # Check if the modality directory exists
            if os.path.exists(modality_dir):
                # Iterate over the files in the modality directory
                for filename in os.listdir(modality_dir):
                    # Check if the filename contains 'spider_msk'
                    if "iso_mod" in filename:
                        pass
                    elif "spider_msk" in filename:
                        # Define the source file path and the target file path
                        source_file = os.path.join(modality_dir, filename)
                        target_file = os.path.join(self.output_dir_labelsTr , f"SPIDER_{subdir.split('-')[1]}.nii.gz")

                        # Copy and rename the file
                        shutil.copy(source_file, target_file)

                        # Append the conversion information to the CSV data
                        self.csv_data.append([source_file, target_file])


        print("labelsTr directory transformation completed.")


    def create_imagesTr_Full_Dataset(self, modalities: list=['T1w', 'T2w']):
        print("Starting imagestTr creation for Full Dataset")

        # Create the target directory if it doesn't exist
        os.makedirs(self.output_dir_imagesTr, exist_ok=True)

        # Iterate over the subdirectories in the source directory
        # for sub in os.listdir(self.input_dir_imagesTr):
        for sub in tqdm(os.listdir(self.input_dir_imagesTr), desc="Processing raw images directories"):

            sub_dir = os.path.join(self.input_dir_imagesTr, sub)
            if os.path.isdir(sub_dir):
                # Iterate over the modalities directories
                for modality in modalities:
                    t_dir_path = os.path.join(sub_dir, modality)
                    if os.path.isdir(t_dir_path):
                        # Iterate over the files in the modality directory
                        for file in os.listdir(t_dir_path):
                            if file.endswith('.nii.gz'):
                                # Construct the new filename and copy the file
                                new_filename = f'{sub}_{modality}_0000.nii.gz'
                                if "acq-iso" in file:
                                    new_filename = f'{sub}_acq-iso_{modality}_0000.nii.gz'
                                shutil.copy(os.path.join(t_dir_path, file), os.path.join(self.output_dir_imagesTr, new_filename))
                                # print(f"File processed: {new_filename}")
                                # Append the conversion information to the CSV data
                                self.csv_data.append([os.path.join(t_dir_path, file), os.path.join(self.output_dir_imagesTr, new_filename)])

        print("imagesTr directory transformation completed.")


    def create_labelsTr_Full_Dataset(self):
        print("Starting labelsTr creation for Full Dataset")

        # Create the target directory if it does not exist
        os.makedirs(self.output_dir_labelsTr , exist_ok=True)

        # Iterate over the subdirectories in the source directory
        # for subdir in os.listdir(self.input_dir_labelsTr):
        for subdir in tqdm(os.listdir(self.input_dir_labelsTr), desc="Processing derivatives directories"):

            # Iterate over the modalities
            for modality in ['T1w', 'T2w']:
                # Define the path to the modality directory
                modality_dir = os.path.join(self.input_dir_labelsTr, subdir, modality)

                # Check if the modality directory exists
                if os.path.exists(modality_dir):
                    # Iterate over the files in the modality directory
                    for filename in os.listdir(modality_dir):
                        # Check if the filename contains 'spider_msk'
                        if "spider_msk" in filename:
                            # Define the source file path and the target file path
                            source_file = os.path.join(modality_dir, filename)
                            if "iso_mod" in filename:
                                target_file = os.path.join(self.output_dir_labelsTr , f"{subdir}_acq-iso_{modality}.nii.gz")
                            else:
                                target_file = os.path.join(self.output_dir_labelsTr , f"{subdir}_{modality}.nii.gz")

                            # Copy and rename the file
                            shutil.copy(source_file, target_file)

                            # Append the conversion information to the CSV data
                            self.csv_data.append([source_file, target_file])

        print("labelsTr directory transformation completed.")



    def save_csv(self):
        # Open the CSV file in write mode
        with open(self.csv_file, mode='w', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the CSV headers
            writer.writerow(self.csv_headers)

            # Write the CSV data
            writer.writerows(self.csv_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert the SPIDER dataset to NNUNet V2 format.')
    parser.add_argument('--full_dataset', type=str, help='If it is the full dataset to be processed.')
    parser.add_argument('--input_dir_imagesTr', type=str, help='The imagesTr path to the directory with the modality .nii.gz. files')
    parser.add_argument('--output_dir_imagesTr', type=str, help='The imagesTr path where the reoriented .nii.gz files are going to be saved.')
    parser.add_argument('--input_dir_labelsTr', type=str, help='The labelsTr path to the directory with the modality .nii.gz. files')
    parser.add_argument('--output_dir_labelsTr', type=str, help='The labelsTr path where the reoriented .nii.gz files are going to be saved.')
    parser.add_argument('--csv_file', type=str, help='The path to save the dataset conversion information.')

    args = parser.parse_args()
    if args.full_dataset == "False":
        # This is to process only one modality: T1W or T2W
        converter = NUUNetDatasetConverter(args.input_dir_imagesTr, args.output_dir_imagesTr, args.input_dir_labelsTr, args.output_dir_labelsTr, args.csv_file)
        converter.create_imagesTr(modality='T2w')
        converter.create_labelsTr(modality='T2w')
    else:
        # This is to process the full dataset, both modalities are included
        converter = NUUNetDatasetConverter(args.input_dir_imagesTr, args.output_dir_imagesTr, args.input_dir_labelsTr, args.output_dir_labelsTr, args.csv_file)
        converter.create_imagesTr_Full_Dataset()
        converter.create_labelsTr_Full_Dataset()
    # Write CSV data
    with open(converter.csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(converter.csv_headers)
        writer.writerows(converter.csv_data)