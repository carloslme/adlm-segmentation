import os
import nibabel as nib
import numpy as np

def get_voxel_volume(nifti_file):
    """Calculate the volume of a voxel in a NIfTI file."""
    img = nib.load(nifti_file)
    header = img.header
    zooms = header.get_zooms()[:3]
    volume = np.prod(zooms)
    return volume

def distribute_files_by_voxel_volume(folder_path, num_groups=10):
    """
    Distribute NIfTI files into groups based on their voxel volume, ensuring equal numbers of files per group.
    
    Args:
        folder_path (str): The path to the folder containing NIfTI files.
        num_groups (int): The number of groups to distribute the files into.

    Returns:
        dict: A dictionary where keys are group numbers and values are lists of file names.
    """
    nifti_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.nii') or f.endswith('.nii.gz')]
    voxel_volumes = [(f, get_voxel_volume(f)) for f in nifti_files]

    if not voxel_volumes:
        print("No NIfTI files found in the specified folder.")
        return {}

    # Sort by voxel volume
    voxel_volumes.sort(key=lambda x: x[1])

    # Calculate the number of files per group
    files_per_group = len(voxel_volumes) // num_groups
    remainder = len(voxel_volumes) % num_groups

    # Distribute files into groups
    groups = {i+1: [] for i in range(num_groups)}
    start_idx = 0
    for i in range(num_groups):
        end_idx = start_idx + files_per_group + (1 if i < remainder else 0)
        groups[i+1] = [os.path.splitext(os.path.basename(f))[0] for f, _ in voxel_volumes[start_idx:end_idx]]
        start_idx = end_idx

    return groups

# Example usage
folder_path = '/vol/aimspace/projects/practical_SoSe24/segmentation/dataset-spider/full-dataset/nnUNet_raw/Dataset000_SPIDER/test/labelsTr'
groups = distribute_files_by_voxel_volume(folder_path)

# Print the distribution
for group, files in groups.items():
    print(f"Group {group}: {len(files)} files")
    for file in files:
        print(f"  - {file}")

# Output the dictionary
print(groups)
