<!-- Intro Text -->
# Setupinit
<b> Properly initialize Python projects </b>

## Table of contents
- [Overview](#overview)
- [Example](#example)
- [API](#api)
- [Project structure](#project-structure)
- [Testing and contributing](#testing-and-contributing)
- [Installation](#installation)


# Overview
**Setupinit** is a command line tool that turns an **empty** directory into a Python project. This tool also ensures that an **existing** Python project is properly initialized. When you run `setupinit init` from the command line, the current working directory is populated with files and folders following the conventional Python project structure as described in the [Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/).


**Setupinit** derives the **project name** from the current working directory, then computes the **package name** from it. The package name is different from the project name. For example, the package name of the `cyberpunk-theme` project is `cyberpunk_theme`. The package name is then used to initialize the contents of certain files such as `setup.cfg`.

**No existing file will be removed or modified by Setupinit**. If, for example, you accidentally corrupted the contents of `setup.cfg`, you can simply manually delete it, then run `setupinit init` from the command line to create a brand new `setup.cfg`.

# Example
**Initialize** an empty Python project:
```bash
$ cd /path/to/project
$ setupinit init
Successfully initialized !
```

Check if a project is **initialized**:
```bash
$ cd /path/to/demo
$ setupinit check
This project is already initialized !
```

# API
**Setupinit** exposes an API (the same used by the CLI) with which you can interact programmatically in Python.

```python
import setupinit

PROJECT_DIR = "/path/to/project"

project_name = setupinit.get_project_name(PROJECT_DIR)

if setupinit.is_initialized(PROJECT_DIR):
    msg = "{} is already initialized.".format(project_name)
    print(msg)
else:
    setupinit.initialize(PROJECT_DIR)
    msg = "{} is initialized !".format(project_name)
    print(msg)

```

> **Read the [modules documentation](https://github.com/pyrustic/setupinit/tree/master/docs/api).**

# Project structure
This is the contents of a newly created Python project with **Setupinit**:

```
demo/  # the demo project ($PROJECT_DIR) [1]
    src
        demo/  # this is the package directory ($PKG_DIR) [2]
            __init__.py
            __main__.py  # the main entry point
    tests/
        __init__.py
        __main__.py
    MANIFEST.in  # already filled with convenient lines of rules
    pyproject.toml  # the new unified Python project settings file [3]
    README.md
    setup.cfg  # you MUST edit this file [4]
    setup.py  # don't remove nor edit this file [5]
    VERSION  # unique location to define the version number [6]
    .gitignore
```

- `[1]` This is the project directory (**$PROJECT_DIR**).
- `[2]` Your codebase lives in the package directory (**$PKG_DIR**).
- `[3]` Read [What the heck is pyproject.toml ?](https://snarky.ca/what-the-heck-is-pyproject-toml/) and the [PEP 518](https://www.python.org/dev/peps/pep-0518/).
- `[4]` Read this [user guide](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html) to edit the `setup.cfg` file.
- `[5]` If you want editable installs you still need a `setup.py` [shim](https://twitter.com/pganssle/status/1241161328137515008).
- `[6]` You won't need to edit this file if you use [Buildver](https://github.com/pyrustic/buildver) to build Python packages.


# Testing and contributing
Feel free to **open an issue** to report a bug, suggest some changes, show some useful code snippets, or discuss anything related to this project. You can also directly email [me](https://pyrustic.github.io/#contact).

## Setup your development environment
Following are instructions to setup your development environment

```bash
# create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# clone the project then change into its directory
git clone https://github.com/pyrustic/setupinit.git
cd setupinit

# install the package locally (editable mode)
pip install -e .

# run tests
python -m tests

# deactivate the virtual environment
deactivate
```

<p align="right"><a href="#readme">Back to top</a></p>

# Installation
**Setupinit** is **cross-platform**. It is built on [Ubuntu](https://ubuntu.com/download/desktop) and should work on **Python 3.8** or **newer**.

## Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

## Install for the first time

```bash
pip install setupinit
```

## Upgrade the package
```bash
pip install setupinit --upgrade --upgrade-strategy eager
```

## Deactivate the virtual environment
```bash
deactivate
```

<p align="right"><a href="#readme">Back to top</a></p>

# About the author
Hello world, I'm Alex, a tech enthusiast ! Feel free to get in touch with [me](https://pyrustic.github.io/#contact) !

<br>
<br>
<br>

[Back to top](#readme)