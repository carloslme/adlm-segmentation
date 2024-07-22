# Convert labels

We only reorient the derivatives folder `derivatives_spider_new` that contains the raw segmentations from the SPIDER dataset.

## Usage

* Access the [convert_labels.sh](shell/convert_labels.sh) script and change the parameters in the lines 21-23 regarding:
  * **--source_dir**: The path to the directory with the original label images.
  * **--target_dir**: The path to the directory where the converted label images will be saved.
  * **--csv_file**: The path to save the labels conversion information.

    So it would be something like this:

    ```bash
    python scripts/convert_labels.py \
        --source_dir ./nnUNet_raw/Dataset000_SPIDER/labelsTr \
        --target_dir ./nnUNet_raw/Dataset000_SPIDER/labelsTr_tmp \
        --csv_file nnUNet_raw/Dataset000_SPIDER/labels_conversion.csv
    ```

* Give execution permission to the shell script

    ```bash
    chmod +x shell/convert_labels.sh
    ```

* Run the script

    ```bash
    shell/convert_labels.sh
    ```

* Inspect the `.segmentation/logs/labels_conversion.log` file.
We should see the print of files processed, and a final line that says:

    ```log
    2024-07-05 17:54:22 | Initializing labels conversion
    Converting labels.
    Starting conversion
    File processed: ./nnUNet_raw/Dataset020_SPIDER/labelsTr_tmp/sub-0112_T1w.nii.gz
    File processed: ./nnUNet_raw/Dataset020_SPIDER/labelsTr_tmp/sub-0191_T1w.nii.gz
    File processed: ./nnUNet_raw/Dataset020_SPIDER/labelsTr_tmp/sub-0058_T2w.nii.gz
    File processed: ./nnUNet_raw/Dataset020_SPIDER/labelsTr_tmp/sub-0011_acq-iso_T2w.nii.gz
    ...
    ```

* You can also inspect the CSV file with the results of conversion that you used in the `--csv_file` parameter.

## Output

The structure remains the same, but if you inspect one file and check the number of labels, you will see only 3 per derivative file.
