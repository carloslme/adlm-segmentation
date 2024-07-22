import os
import json
import argparse

def create_json(directory, output_file):
    num_training = len([f for f in os.listdir(directory) if f.endswith('.nii.gz')])
    
    data = {
        "channel_names": {
            "0": "T1W"
        },
        "labels": {
            "background": 0,
            "vertebral": 1,
            "intervertebral": 2,
            "spinal-canal": 3
        },
        "numTraining": num_training,
        "file_ending": ".nii.gz"
    }
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a JSON file with dataset information.')
    parser.add_argument('--directory', type=str, help='Path to the directory containing .nii.gz files')
    parser.add_argument('--output_file', type=str, help='Output JSON file path')
    
    args = parser.parse_args()
    
    create_json(args.directory, args.output_file)
