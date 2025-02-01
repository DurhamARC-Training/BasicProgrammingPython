# Learning to programme with python

Welcome to the Course "Learning to programme with python" repository! This repository contains all the materials and resources for the course.

## Organization

The repository is organized as follows:

- `Basic.ipynb`: The course's jupyter notebook with the corresponding materials.

- `Basic_filled.ipynb`: The course's jupyter notebook with all the material filled in. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during the course.

- `pull_files_from_repo.py`: download script that can be executed to extract this repository into a folder.

## Getting Started as student
If you want to set up a new conda environment for the course you can use the environment.yml provided in this folder.

There are three possibilities to get the data:

1. You only want to follow along. Just download and copy the Basics.ipynb to your environment

2. To get everything (including the filled notebook) 

      a. Download the `pull_files_from_repo.py` file and put it into your environment

      b. Execute `python pull_files_from_repo.py` in the folder.

3. If you have git available you can just clone the repo with:

   `git clone https://github.com/DurhamARC-Training/BasicProgrammingPython.git`

## Getting Started for Teaching

To get started with teaching the course, follow these steps:

1. Install the requirements including JupyterLab Deck by running the following command:

    ```
    conda env create -f environment.yml
    ```

2. Launch JupyterLab by running the following command:

    ```
    conda activate basic_python
    jupyter lab
    ```

3. Use the `Basics.ipynb` for the presentations and exercises to use during the course. If needed use the notebooks use the `Basics_filled.ipynb` as lecture notes

4. Click on the little card styles JupyterLab-Deck icon for running a notebook as a presentation.

5. It is also possible to convert the Jupyter notebook to PDF (be sure first to run all cells you want to run and save):

   * Call `jupyter nbconvert --to slides --post serve .\Basics.ipynb`
   * Go to http://localhost:8000/Basics.slides.html?print-pdf#/
   * Print via Print to PDF function of your browser


## How to contribute

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!

If you're a co-developer of our training course, please read the workflow we suggest on this [contribution page](development.md).