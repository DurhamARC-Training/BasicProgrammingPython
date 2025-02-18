# Developer's Guide

This section explains the workflow how to modify and update the Jupyter notebooks.

## Structure and workflow

The repository is organised as follows:

- `Basic.ipynb`: The course's Jupyter notebook with the corresponding materials.

- `Basic_filled.ipynb`: The course's Jupyter notebook with all the material filled in. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during the course.

Modifications can still be made directly in the Jupyter notebooks as before. However, any change in one notebook requires a manual update in the other to keep their versions aligned. Another drawback is that version control for Jupyter notebooks can be challenging because they often track more than just the course content—such as metadata—despite our wanting to track only the course material. This is precisely why we use Markdown equivalents of the Jupyter notebooks: they simplify version control by focusing solely on the content and ignoring the notebooks’ metadata.

- `Basics.md`: this is the `Basic.ipynb` notebook (without solutions) converted into Markdown format.

- `Basics_filled.md`: this is the `Basic_filled.ipynb` notebook (with solutions) converted into Markdown format.

The idea is to edit only the full `Basics_filled.md`, while a small Python script (`filter_md.py` from our other repository, see below how to get it) automatically generates `Basics.md` by removing the solutions. This approach keeps both files aligned without requiring manual updates.

However visually, it might be still easier to edit Jupyter notebooks rather than Markdown files. Therefore, a following workflow is suggested before submitting the changes to the repository:

1. Edit the Jupyter notebook with solutions (`Basic_filled.ipynb`) as usual.
2. Convert the Jupyter notebook into Markdown by running Jupytext. This command will generate a Markdown version of the Jupyter notebook:
    ```bash
    jupytext --to md Basics_filled.ipynb
    ```
3. Mark any solution cells you’ve added (that aren’t already marked) in the Markdown file with the start and end markers recognised by the provided `filter_md.py` script, as shown:
    ```markdown
    <!-- #solution -->
    <!-- #endsolution -->
    ```
4. Now it's time to update the no-solutions python notebooks:
    - Firstly, add our other repository containing common tools for preparing teaching materials:
        ```bash
        git submodule add https://github.com/DurhamARC-Training/common-tools.git common-tools
        ```
    - Run the `filter_md.py` script from the `common-tools-for-teaching` submodule (added as a git submodule folder `common`) to remove the blocks with solutions, specifying the “full” (solution-inclusive) Markdown filename and your desired "no-solutions" output filename:
        ```bash
        python common/filter_md.py Basics_filled.md Basics.md
        ```
5. Convert both Markdown files back to Jupyter notebooks:
    ```bash
    jupytext --to notebook Basics_filled.md
    jupytext --to notebook Basics.md
    ```
6. Now, instead of committing Jupyter notebooks directly, you commit their Markdown versions to the version control system (though you can still keep the Jupyter notebooks for convenience).

To simplify a bit the end of the workflow (to combine steps 4-6), a bash script `generate_notebooks.sh` can be run to execute these steps all at once.