###### Setupinit API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/setupinit/__init__/README.md) | [Source](/src/setupinit/__init__.py)

# Functions within module
> Module: [setupinit.\_\_init\_\_](/docs/api/modules/setupinit/__init__/README.md)

Here are functions exposed in the module:
- [\_update\_setup\_cfg](#_update_setup_cfg)
- [get\_missing\_files](#get_missing_files)
- [get\_pkg\_name](#get_pkg_name)
- [get\_project\_name](#get_project_name)
- [get\_required\_filenames](#get_required_filenames)
- [initialize](#initialize)
- [is\_initialized](#is_initialized)

## \_update\_setup\_cfg
No docstring

```python
def _update_setup_cfg(data, project_dir):
    ...
```

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## get\_missing\_files
Returns a dict of missing required files in a project

```python
def get_missing_files(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, the path to the project root. By default, os.getcwd is called |

### Value to return
Returns a dict of missing filenames.
The keys of the dict are the canonical names of the missing files.
The values are missing filenames (obviously these filenames doesn't exist).
Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## get\_pkg\_name
This function extracts the application package name from a project_dir.
Basically it extracts the basename from the path then turns dashes "-" into
"underscores" "_".

```python
def get_pkg_name(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, path to the target project |

### Value to return
str, the application package name.

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## get\_project\_name
This function returns the project name.
Basically it extracts the basename from the path

```python
def get_project_name(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, path to the target project |

### Value to return
str, the project name.

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## get\_required\_filenames
Returns a dict of required filenames.

```python
def get_required_filenames(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, the path to the project root. By default, os.getcwd is called |

### Value to return
Returns a dict.
The keys of the dict are the canonical names of the required files.
The values are filenames as they should be if these files exist.
Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## initialize
Initialize a project by populating it with required files and directories.
These files are pre-filled with useful data.

```python
def initialize(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, the path to the project root. By default, os.getcwd is called |

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>

## is\_initialized
Check if a Python project is initialized.
This function checks the files present in the root against a list of
required filenames (see the function: get_required_filenames())

```python
def is_initialized(project_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| project\_dir | str, the path to the project root. If you don't set a path, the value of 'os.getcwd()' will be used |

### Value to return
Returns True if the project is initialized, else returns False

<p align="right"><a href="#setupinit-api-reference">Back to top</a></p>
