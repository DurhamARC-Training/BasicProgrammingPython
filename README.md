![Course logo](img/ARC448p.png)

# Course: Learning to programme with python

Welcome to the Learning to programme with python repository! This repository contains all the materials and resources for the course.

## Course description

If you've never written a line of code but suspect programming might benefit your research, this course provides a gentle introduction through Python. Designed for complete beginners, we'll cover fundamental programming concepts, ensuring everyone builds solid foundations regardless of technical background.
The course takes a hands-on approach using Jupyter notebooks to explore essential programming elements: basic data types (strings, integers, floats, booleans), variables, operators, and control flow statements including if-statements and loops. You'll learn to write functions, handle user input, read and write files, and work with data structures like lists.
By the end, you'll understand how basic computer programs work, how to structure code effectively, and where to find resources for continued learning. There will be plenty of opportunities to experiment and ask questions throughout. No prior experience required, just curiosity about what programming can do.

## Organization

The repository is organized as follows:

- `Basics.ipynb`: This file contains the course material we will be using during the course

- `Basics_filled.ipynb`: This file contains the completed course material, the solutions to the exercises and the speaker notes. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during teaching.


## Accessing the Materials

For this course we are using [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/), which is a tool that allows us to launch [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) and run our Python code in the web browser through the notebook (.ipynb) files contained in this repository.

To access and run the course materials, start by:

* Navigating to the course materials on our GitHub page: [https://durhamarc-training.github.io/BasicProgrammingPython/](https://durhamarc-training.github.io/BasicProgrammingPython/)

* Start by accessing `Basics.ipynb` notebook.

You are now ready to start the course!

NOTE: The first time you run your code/load new modules, there may be a small wait while the module(s) are loaded.

## Contributing

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!

You can add the files of the `common-tools` github submodule by typing in `git submodule update --init`. Consult the README in the then filled `common-tools` directory for further instructions.
In general you should never edit the content in the `Basics.ipynb` but work on `Basics_filled.ipynb` and have the tool generate the student notebook versions automatically as described in the `common-tools` README.
