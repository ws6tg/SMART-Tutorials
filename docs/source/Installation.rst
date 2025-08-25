Installation
============

| The **SMART** package is developed based on the PyTorch framework and
  supports execution on both CPU and GPU.
| Using a GPU is strongly recommended, as it can significantly
  accelerate the integration process.

To enable GPU acceleration, please ensure that **PyTorch** and **CUDA
(including cuDNN)** are properly installed, along with the appropriate
GPU drivers for your system.

--------------

Software dependencies
---------------------

To run the SMART package, make sure all dependencies listed in
``requirements.txt`` are installed:

.. code:: bash

   muon==0.1.6 
   scanpy==1.10.2 
   scikit-learn==1.5.1 
   anndata==0.10.8 
   matplotlib==3.9.2 
   tqdm==4.66.5 
   numba==0.60.0 
   rpy2==3.5.12 
   torch==2.4.1 
   torch_geometric==2.3.0
   harmony-pytorch==0.1.8
   scikit-misc==0.3.1

Environment setup
-----------------

We recommend creating a dedicated conda environment for SMART:

.. code:: 

   # 1. create conda environment
   conda create -n smart python=3.9.23 -y

   # 2. activate conda environment
   conda activate smart

   # 3. Install R
   conda install -c conda-forge r-base=4.3.0 -y

   # 4. Install Python dependencies
   pip install -r requirements.txt

In addition, you need to install the **mclust** R package:

.. code:: 

   # 1. Activate the conda environment
   conda activate smart
   # 2. Start the R console
   R
   # 3. Install the mclust package
   install.packages("mclust", repos = "https://cloud.r-project.org")
   # 4. Exit the R console
   q()

Install SMART via pip
---------------------

You can install SMART directly from PyPI:

.. code:: 

   pip install bio-SMART

After installation, verify it by importing SMART and checking its
version:

.. code:: 

   import smart 
   print(smart.__version__)  # check installation

If the installation is successful, the version number of SMART will be
printed.
