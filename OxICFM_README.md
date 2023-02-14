# connect to ARC

in mobaXterm or powershell (Windows) or terminal (Mac/Linux)
        ssh teachingXX@arc-login.arc.ox.ac.uk

use the password associated with your account (emailed)

# Download the demo files from GitHub

        git clone --recursive https://github.com/MorrowChem/how-to-validate-potentials-demo.git

        cd how-to-validate-potentials-demo

        git checkout remotes/origin/OxICFM_workshop  # this is the branch for the workshop

# Download Python

        cd ../ 

        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

        bash Miniconda3-latest-Linux-x86_64.sh # follow the prompts, accept the defaults

copy and paste the line that looks like:

        eval "$(/home/teaching12/miniconda3/bin/conda shell.YOUR_SHELL_NAME hook)"

changing YOUR_SHELL_NAME to bash

# Install python packages

        conda create -n -y cdt python=3.8 pip jupyterlab

        conda activate cdt

        pip install -r requirements.txt

# Jump on to the compute node

        srun --nodes=1 --ntasks-per-node=40 --partition=interactive --pty /bin/bash --time:04:00:00

you should see something like `(base) [teachingXX@arc-c304` at the start of the line instead of `arc-login`

# Start a jupyter server

        conda activate cdt

        jupyter-notebook --no-browser --port=8888 &

# Connect to the jupyter server on your local machine
run this command in a new shell on your local machine (not on ARC). Make sure you change the XXXs to your username and node number.

        ssh -N -f -L 8888:arc-cXXX:8888 teachingXX@arc-login.arc.ox.ac.uk

# Open the jupyter server in your browser
open a browser on your local machine and go to the following address (the token is printed in the terminal on ARC)

        http://localhost:8888/?token=XXX