# Bonus chapter

## How to run python on your own computer

If you wish to run exercise locally, you can certainly install Python and Jupyter interactive notebook on your own laptop, see the installation instructions below.

### Installing Python

#### On Windows:

1. Go to https://www.python.org/downloads/) and choose the latest stable installer for Windows (for example, “Windows installer (64-bit)”).
2. During installation, make sure to check the box “Add Python to PATH” so you can use Python from any command prompt.
3. After installation finishes, open a new Terminal (Command Prompt or PowerShell) and type:

```
python --version
```

This should confirm that Python installed successfully.

  - Alternatively, you could install the Anaconda distribution from https://www.anaconda.com/products/distribution, which includes Python and a variety of data-science packages by default.

#### On Linux (Ubuntu/Debian-based):

1. Open a terminal.
2. Run:
```
sudo apt-get update
sudo apt-get install python3 python3-pip
```
(Adjust to python or python3 depending on your distribution)

1. Confirm your installation by running:
```
python3 --version
```

  - For Fedora or other distributions, replace `apt-get` with `yum`, `dnf`, or your distro’s package manager.
  - You can also install Anaconda if you want a more complete environment.


#### On macOS:

1. Visit https://www.python.org/downloads/ and download the macOS installer (e.g., “macOS 64-bit universal2 installer”).
2. Double-click the `.pkg` file and follow the prompts.
3. After installation, open Terminal and check:
```
python3 --version
```

  - Alternatively, on macOS you can install Python via Homebrew (if you already have Homebrew installed) by running:
```
brew install python3
```

#### Installing and Running Jupyter Notebooks

1. Once Python is installed (whether from python.org, your Linux package manager, or Anaconda), you can install Jupyter Notebook as follows:
```
pip install jupyter
```

Or Jupyter Lab, the next-generation web-based interface for the Jupyter project (which I'll be using)
```
pip install jupyterlab
```
(Use `pip3` if needed, e.g., › `pip3 install jupyter`) • If you chose Anaconda, Jupyter Notebook is already included, so you can skip this step.

2. When everything is installed, you can start a Jupyter notebook server (or Jupyter Lab) and work on your Python exercises by simply running in your terminal or command prompt:
```
jupyter notebook
```
or
```
jupyter lab
```

This will open a new tab in your web browser with the Jupyter Notebook or Jupyter Lab interface, ready for you to start coding!