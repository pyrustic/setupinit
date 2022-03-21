<!-- Intro Text -->
# Setupinit
<b> Properly initialize a Python project </b>
    
This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/setupinit/tags) . [Documentation](https://github.com/pyrustic/setupinit/tree/master/docs/modules#readme)

## Table of contents
- [Overview](#overview)
- [Example](#example)
- [API](#api)
- [Project structure](#project-structure)
- [Related projects](#related-projects)
- [Installation](#installation)


# Overview
**Setupinit** is a command line tool that turns an **empty** directory into a Python project. This tool also ensures that an **existing** Python project is properly initialized. When you run `setupinit init` from the command line, the current working directory is populated with files and folders following the conventional Python project structure as described in the [Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/). 

**Setupinit** derives the **project name** from the current working directory, then computes the **package name** from it. The package name is different from the project name. For example, the package name of the `cyberpunk-theme` project is `cyberpunk_theme`. The package name is then used to initialize the contents of certain files like `setup.cfg`.

As a developer, you remain in control of your project, so no existing file will be modified by **Setupinit**. If, for example, you accidentally corrupted the contents of `setup.cfg`, you can simply delete it, then run `setupinit init` from the command line to create a brand new `setup.cfg`.

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

if setupinit.initialized(PROJECT_DIR):
    msg = "{} is already initialized.".format(project_name)
    print(msg)
else:
    setupinit.initialize(PROJECT_DIR)
    msg = "{} is initialized !".format(project_name)
    print(msg)

```

> **Read the [modules documentation](https://github.com/pyrustic/setupinit/tree/master/docs/modules#readme).**

# Project structure
This is the contents of a newly created Python project with **Setupinit**:

```
demo/  # the demo project ($PROJECT_DIR) [1]
    demo/  # this is the app package ($APP_PKG) [2]
        __init__.py
        __main__.py  # the mighty entry point of your app !
    tests/
        __init__.py
    MANIFEST.in  # already filled with convenient lines of rules
    pyproject.toml  # the new unified Python project settings file [3]
    README.md
    setup.cfg  # define here your name, email, dependencies, and more [4]
    setup.py  # it is not a redundancy, don't remove it, don't edit it [5]
    VERSION  # unique location to define the version of the app [6]
    .gitignore  # you can edit it if you want
```

- `[1]` This is the project directory (**$PROJECT_DIR**).
- `[2]` Your codebase lives in the app package (**$APP_PKG**).
- `[3]` Read [What the heck is pyproject.toml ?](https://snarky.ca/what-the-heck-is-pyproject-toml/) and the [PEP 518](https://www.python.org/dev/peps/pep-0518/).
- `[4]` Read this [user guide](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html) to edit the `setup.cfg` file.
- `[5]` If you want editable installs you still need a `setup.py` [shim](https://twitter.com/pganssle/status/1241161328137515008).
- `[6]` You won't need to edit this file if you use **Backstage** or **Buildver** a command line tool with a built-in intuitive versioning mechanism.

You can even run this new project:

```bash
$ cd /path/to/demo
$ python -m demo
Hello Friend !
```

# Related projects
For a smooth developer experience, you can try related projects: **buildver** and **backstage**.

## Buildver
**Buildver** is a command line tool to build a Python distribution package from a project. This tool comes with a **built-in versioning mechanism** that works smoothly with the package builder while being intuitive for the user.

> **Discover [Buildver](https://github.com/pyrustic/buildver) !**

## Backstage
**Backstage** is a **language-agnostic** command line tool that allows the developer to define, coordinate, and use the various resources at his disposal to create and manage a software project.

> **Discover [Backstage](https://github.com/pyrustic/backstage) !**

# Installation
**Setupinit** is **cross platform** and versions under **1.0.0** will be considered **Beta** at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.

## For the first time

```bash
$ pip install setupinit
```

## Upgrade
```bash
$ pip install setupinit --upgrade --upgrade-strategy eager

```

<br>
<br>
<br>

[Back to top](#readme)
