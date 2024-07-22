#!/usr/bin/env python3

import os
import numpy as np
import nibabel as nib
import argparse
import csv

class LabelConverter:
    def __init__(self, source_dir, target_dir, csv_file):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.csv_file = csv_file

    def convert_labels(self):
        print("Starting conversion")
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
        for file in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, file)
            if file.endswith('.nii') or file.endswith('.nii.gz'):
                nii_image = nib.load(file_path)
                data = nii_image.get_fdata()

                # Convert data based on new specifications
                converted_data = np.zeros_like(data, dtype=np.uint8)
                converted_data[(data >= 1) & (data <= 9)] = 1
                converted_data[data == 100] = 2
                converted_data[(data >= 201) & (data <= 209)] = 3

                new_nii_image = nib.Nifti1Image(converted_data, nii_image.affine, nii_image.header)
                new_file_path = os.path.join(self.target_dir, file)
                nib.save(new_nii_image, new_file_path)
                print("File processed:", new_file_path)

                # Save results in a CSV file
                csv_file = os.path.join(self.csv_file)
                with open(csv_file, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file_path, new_file_path])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert the labels images in the SPIDER dataset derivatives (segmentations) to three labels')
    parser.add_argument('--source_dir', type=str, help="The path to the directory with the original label images")
    parser.add_argument('--target_dir', type=str, help="The path to the directory where the converted label images will be saved")
    parser.add_argument('--csv_file', type=str, help='The path to save the labels conversion information.')
    args = parser.parse_args()
    
    converter = LabelConverter(source_dir=args.source_dir, target_dir=args.target_dir, csv_file=args.csv_file)
    converter.convert_labels()