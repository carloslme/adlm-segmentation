import os
import csv
import nibabel as nib
import argparse

class DataValidator:
    def __init__(self, csv_file, report_file):
        self.csv_file = csv_file
        self.report_file = report_file

    def validate_data(self):
        # Open the CSV file in read mode
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header

            # Open the report file in write mode
            with open(self.report_file, 'w', newline='') as report:
                writer = csv.writer(report)
                # Write the header
                writer.writerow(["Input File Directory", "Output File Directory", "Source Shape", "Target Shape", "Source Voxel Space", "Target Voxel Space", "Status"])

                # Iterate over the rows in the CSV file
                for row in reader:
                    # Get the source file path and the target file path
                    source_file = row[0]
                    target_file = row[1]

                    # Check if the source file and the target file exist
                    if os.path.exists(source_file) and os.path.exists(target_file):
                        # Load the source file and the target file
                        source_img = nib.load(source_file)
                        target_img = nib.load(target_file)

                        # Get the shape, the size, and the voxel space of the source file and the target file
                        source_shape = source_img.shape
                        target_shape = target_img.shape
                        source_voxel_space = source_img.header.get_zooms()
                        target_voxel_space = target_img.header.get_zooms()

                        # Check if the shape, the size, and the voxel space are the same
                        if source_shape == target_shape and source_voxel_space == target_voxel_space:
                            status = "Valid"
                        else:
                            status = "Invalid"

                        # Write the data to the CSV file
                        writer.writerow([source_file, target_file, source_shape, target_shape, source_voxel_space, target_voxel_space, status])

        print("Validation completed. Report saved to", self.report_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate the files converted are the same as the raw ones (different names, but voxel space is the same).')
    parser.add_argument('--csv_file', type=str, help='The path where the dataset conversion information was saved.')
    parser.add_argument('--report_file', type=str, help='The path to save the dataset validation.')

    args = parser.parse_args()
    csv_file = "/vol/aimspace/projects/practical_SoSe24/segmentation/dataset-spider/full-dataset/full_dataset_conversion_results.csv"
    report_file = "/vol/aimspace/projects/practical_SoSe24/segmentation/dataset-spider/full-dataset/validation_full_dataset.csv"
    validator = DataValidator(args.csv_file, args.report_file)
    validator.validate_data()