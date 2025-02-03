#!/usr/bin/bash

# This is the script to run after modification of "Basics_filled.md" are done

# Execute "filter_md.py" which reads 
# "Basics_filled.md" (with solutions) and produces
# "Basics.md" (without solutions)
python filter_md.py Basics_filled.md Basics.md

# Convert both Markdown files into Jupyter notebooks
jupytext --to notebook Basics_filled.md
jupytext --to notebook Basics.md

