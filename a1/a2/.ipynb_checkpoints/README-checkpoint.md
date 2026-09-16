# LIS 4369 - Assignment 2
## Summary
In this assignment, I set up a custom Conda environment named testenv to manage dependencies for Python data analytics. I also configured the environment as a custom kernel in JupyterLab so I can select it directly inside my notebooks

## Reference Materials
Python_Environments.pdf: Reviewed this guide to understand virtual environments, package installation, and keeping project dependencies isolated
conda-cheat-sheet.pdf: Used as a quick reference for Conda terminal commands
my_env_versions_py.png: Screenshot confirming the terminal output after running my_env_versions.py in the activated testenv environment

## What I Did
1. Created the testenv Conda environment using testenv.yml
2. Activated the environment in the terminal
3. Ran python my_env_versions.py to confirm that all required packages installed correctly
4. Installed ipykernel and registered testenv so it appears as a selectable kernel in JupyterLab

## Included Files
- A2.ipynb - Assignment notebook running on the Python (testenv) kernel.
- testenv.yml - Conda environment file.
- my_env_versions.py - Script checking installed package versions.
- my_env_versions_py.png - Screenshot of script output in terminal.
- README.md - Documentation file.