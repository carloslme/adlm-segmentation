# Setup `venv`

The order of the following instructions is important!

* Create a directory called `segmentation` and change the directory.
* Run the following commands, these will install the environment under the directory you are working with:

    ```bash
    mkdir -p ./<YOUR-ENV>
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./<YOUR-ENV>/miniconda.sh
    bash ./<YOUR-ENV>/miniconda.sh -b -u -p ./<YOUR-ENV>
    rm -rf ./<YOUR-ENV>/miniconda.sh
    ```

* After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

    ```bash
    ./<YOUR-ENV>/bin/conda init bash
    ./<YOUR-ENV>/bin/conda init zsh
    ```

* Verify if the environment exists.

    ```bash
    conda info --envs
    ```

    You should see something like:

    ```bash
    
    `conda environments:# base`
    
    `../segmentation/<YOUR-ENV>`
    ```

* You can rename create an “alias” to the virtual environment running this code

    ```bash
    conda rename -p ../segmentation/<YOUR-ENV> <YOUR-ENV>
    ```

    This will allow you to use only the alias instead of the full path.
