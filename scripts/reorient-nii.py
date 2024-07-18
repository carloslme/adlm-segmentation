'''
This script reorients all the .nii.gz files in a directory to the RAS orientation and saves them in a new directory.
'''

import os
import nibabel as nib
from TPTBox import *
import csv
import argparse

class NiiReorient:
    def __init__(self, input_dir, output_dir, csv_file):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.csv_file = csv_file


    def reorient_files(self, current_dir):
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Open the CSV file for writing
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["Input Directory", "Output Directory", "Original Orientation", "Output Orientation"])

            for root, dirs, files in os.walk(current_dir):
                for file in files:
                    if file.endswith('.nii.gz'):
                        # Load the nii.gz file
                        file_path = os.path.join(root, file)
                        nii = NII(nib.load(file_path))
                        original_orientation = nii.orientation
                        if original_orientation != ("R", "A", "S"):
                            nii.reorient_(("R", "A", "S"), verbose=True) 

                        # Save the reoriented image with the original file name in the output directory
                        relative_path = os.path.relpath(root, self.input_dir)
                        output_path = os.path.join(self.output_dir, relative_path, file)
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        nii.save(output_path)
                        # visualize_image(output_path)

                        # Write the reorientation information to the CSV file
                        writer.writerow([file_path, output_path, original_orientation, nii.orientation])

        print("Reorientation complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Reorient an MRI scan and save it.')
    parser.add_argument('--input_dir', type=str, help='The path to the directory with the .nii.gz. files')
    parser.add_argument('--output_dir', type=str, help='The path where the reoriented .nii.gz files are going to be saved.')
    parser.add_argument('--csv_file', type=str, help='The path to save the reorientation information.')

    args = parser.parse_args()
    
    reorienter = NiiReorient(args.input_dir, args.output_dir, args.csv_file)
    reorienter.reorient_files(args.input_dir)

