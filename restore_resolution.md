# Restore resolution

In order to perform the evaluation, we need to restore to the native resolution, follow the next steps to restore to the native resolution.

## Usage

### 1x1x1

* Open the [restore-resolution-1x1x1-full](shell/restore/restore-resolution-1x1x1-full.sh) file and ensure the lines from 20 to 26 make sense to your configuration.

* Give execution permission to the shell script

    ```bash
    chmod +x shell/restore/restore-resolution-1x1x1-full.sh
    ```

* Run the script

    ```bash
    shell/restore/restore-resolution-1x1x1-full.sh
    ```

## Output

You will see in a folder called `nativeres_250` the files with the origin resolution.

## What about the other folders?

You can repeat the steps above for other resolutions such as `3x1x1`, `2.1x0.7x0.7`, etc.
