import os
import shutil
import argparse
import ast

def move_files(src_dir, output_dir, list_files):
    # Create destination directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert string representation of list to actual list
    list_files = ast.literal_eval(list_files)

    # Iterate over files in source directory
    for filename in os.listdir(src_dir):
        # Extract subject ID from filename
        subject_id = filename.split('_')[0].split('-')[1]
        # Check if subject ID is in the list of IDs
        if subject_id in list_files:
            # Construct full file paths
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(output_dir, filename)
            # Move file to destination directory
            shutil.move(src_file, dst_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Move files based on a list of IDs.')
    parser.add_argument('--imagesTr_dir', required=True, help='Path to the imagesTr directory')
    parser.add_argument('--imagesTr_output_dir', required=True, help='Path to the output directory for imagesTr')

    parser.add_argument('--labelsTr_dir', required=True, help='Path to the labelsTr directory with 4 labels converted.')
    parser.add_argument('--labelsTr_output_dir', required=True, help='Path to the output directory for labelsTr with 4 labels converted.')

    parser.add_argument('--labelsTr_dir_native', required=False, help='Path to the 15 labels directory')
    parser.add_argument('--labelsTr_output_dir_native', required=True, help='Path to the output labelsTr directory for the 15 labels.')

    parser.add_argument('--list_files', required=True, help='String representation of a list of file IDs to move')

    args = parser.parse_args()

    move_files(args.imagesTr_dir, args.imagesTr_output_dir, args.list_files)
    move_files(args.labelsTr_dir, args.labelsTr_output_dir, args.list_files)
    move_files(args.labelsTr_dir_native, args.labelsTr_output_dir_native, args.list_files)