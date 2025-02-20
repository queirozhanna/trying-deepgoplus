# Downloading the Miniconda executable
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Allowing the installing of the executer 
$ chmod +x Miniconda3-latest-Linux-x86_64.sh

# Executing the installer
$ ./Miniconda3-latest-Linux-x86_64.sh

# Executing the miniconda's environment
$ ./miniconda3/bin/conda init

# CLose the terminal and open again. If there's "(base)" before the username, it means that the previous processes have worked.

# Creating a conda environment with Python 3.7 
$ conda create -n "env_python3.7" python=3.7 -c conda-forge

# Activating the environment 
$ conda activate env_python3.7

# Verifying if the created environment really is a Python 3.7 environment 
$ sudo add-apt-repository ppa:deadsnakes/ppa
  # If it's not Python 3.7 
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt update
    $ apt list --upgradable
    $ sudo apt install python3.7
    $ sudo apt install python3.7-venv python3.7-dev python3-pip
    $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

# Cloning DeepGOPlus gitHub repository 
$ git clone https://github.com/bio-ontology-research-group/deepgoplus.git

# Opening the cloned folder
$ cd deepgoplus/

# Installing the dependencies
  # absl-py==0.6.1
  # astor==0.7.1
  # Click==7.1.2            
  # Cython==0.29.14
  # gast==0.2.1
  # grpcio==1.17.1
  # h5py==2.9.0
  # Keras-Applications==1.0.6
  # Keras-Preprocessing==1.0.5
  # Markdown==3.0.1
  # matplotlib==3.3.2        
  # numpy==1.18.5           
  # pandas==1.1.2           
  # protobuf==3.6.1
  # python-dateutil==2.7.5
  # pytz==2018.7
  # requests==2.24.0         
  # scikit-learn==0.20.2
  # scipy==1.2.0
  # six==1.12.0
  # sklearn==0.0
  # tensorboard==1.12.2
  # tensorflow-gpu==2.3.1    
  # termcolor==1.1.0
  # Werkzeug==0.14.1
  # wget==3.2               
  # word2vec==0.10.2

# Installing Diamond:
$ conda install bioconda::Diamond

# Installing DeepGOPlus:
$ pip install deepgoplus
