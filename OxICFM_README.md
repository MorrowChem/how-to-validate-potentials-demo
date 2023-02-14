This is a set of instructions for connecting to the University High-Performance Computing (HPC) cluster, ARC, and running the demo notebooks for the OxICFM CDT Advanced Solids workshop.

ARC uses a linux operating system, like most HPC clusters, and has no GUI, only a command-line. I recommend getting familar with the basics of running commands in a BASH terminal by reading through this briefly if you get stuck, or if you want to learn more about what the following recipe is doing: 

        https://linuxconfig.org/bash-scripting-tutorial-for-beginners


# connect to ARC

in mobaXterm or powershell (Windows) or terminal (Mac/Linux)

        ssh teachingXX@arc-login.arc.ox.ac.uk

use the username and password associated with your account (emailed)

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

changing **YOUR_SHELL_NAME** to **bash**

# Install python packages

        conda create -y -n cdt python=3.8 pip jupyterlab cmake

        conda activate cdt

        pip install -r requirements.txt

# Jump on to the compute node
make sure your ~/.bash_profile file has the chem20XXXX reservation instead of teaching

        srun --nodes=1 --ntasks-per-node=40 --time=04:00:00 --pty /bin/bash

you should see something like `(base) [teachingXX@arc-c304` at the start of the line instead of `arc-login`

# Start a jupyter server

        conda activate cdt

        jupyter-notebook --no-browser --ip=* &

# Connect to the jupyter server on your local machine
run this command in a new shell on your local machine (not on ARC). Make sure you change the **XXX**s to your username and node number.

        ssh -L 8080:arc-cXXX:8888 teachingXX@arc-login.arc.ox.ac.uk

# Open the jupyter server in your browser
open a browser on your local machine and copy and paste the address from your terminal on ARC that looks like the below. Notice the change of the port number from 8888 to 8080 -- you need to do this manually

        http://localhost:8080/?token=XXX

your *token* will also be in the terminal on ARC around the same place

# Open the notebook and start the exercises

1. demo-lammps.ipynb

2. demo-validation-soap.ipynb

Instructions and explanations are in the notebooks, which you can run in the browser. The python code is running on a node on ARC (48 CPUs of computing power!) Let me know if you have any questions.

Here is an intro to Jupyter Notebooks if you are not familiar with them:

https://www.dataquest.io/blog/jupyter-notebook-tutorial/
