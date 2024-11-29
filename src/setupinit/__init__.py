import os
import os.path
import pkgutil


def is_initialized(project_dir=None):
    """
    Check if a Python project is initialized.
    This function checks the files present in the root against a list of
    required filenames (see the function: get_required_filenames())

    [params]
    - project_dir: str, the path to the project root.
    If you don't set a path, the value of 'os.getcwd()' will be used

    [returns]
    Returns True if the project is initialized, else returns False
    """
    if not project_dir:
        project_dir = os.getcwd()
    required_filenames = get_required_filenames(project_dir)
    for filename in required_filenames.values():
        if not os.path.isfile(filename):
            return False
    return True


def get_missing_files(project_dir=None):
    """Returns a dict of missing required files in a project

    [params]
    - project_dir: str, the path to the project root. By default, os.getcwd is called

    [returns]
    Returns a dict of missing filenames.
    The keys of the dict are the canonical names of the missing files.
    The values are missing filenames (obviously these filenames doesn't exist).
    Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}
    """
    if not project_dir:
        project_dir = os.getcwd()
    cache = dict()
    required_filenames = get_required_filenames(project_dir)
    for key, value in required_filenames.items():
        if not os.path.isfile(value):
            cache[key] = value
    return cache


def initialize(project_dir=None):
    """
    Initialize a project by populating it with required files and directories.
    These files are pre-filled with useful data.

    [params]
    - project_dir: str, the path to the project root. By default, os.getcwd is called
    """
    project_dir = project_dir if project_dir else os.getcwd()
    required_filenames = get_required_filenames(project_dir)
    for key, filename in required_filenames.items():
        if os.path.isfile(filename):
            continue
        # make directory
        parent_dir = os.path.dirname(filename)
        if not os.path.isdir(parent_dir):
            os.makedirs(parent_dir)
        # create file
        res = "/default_files/{}".format(key)
        data = pkgutil.get_data("setupinit", res)
        if key == "setup_cfg":
            data = _update_setup_cfg(data, project_dir)
        with open(filename, "wb") as file:
            file.write(data)


def get_required_filenames(project_dir=None):
    """Returns a dict of required filenames.

    [params]
    - project_dir: str, the path to the project root. By default, os.getcwd is called

    [returns]
    Returns a dict.
    The keys of the dict are the canonical names of the required files.
    The values are filenames as they should be if these files exist.
    Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}
    """
    project_dir = project_dir if project_dir else os.getcwd()
    # pkg_name
    pkg_name = get_pkg_name(project_dir)
    # src
    src_dir = os.path.join(project_dir, "src", pkg_name)
    project_init_py = os.path.join(src_dir, "__init__.py")
    project_main_py = os.path.join(src_dir, "__main__.py")
    # tests
    tests_dir = os.path.join(project_dir, "tests")
    tests_init_py = os.path.join(tests_dir, "__init__.py")
    tests_main_py = os.path.join(tests_dir, "__main__.py")
    # MANIFEST.in
    manifest = os.path.join(project_dir, "MANIFEST.in")
    # pyproject.toml
    pyproject_toml = os.path.join(project_dir, "pyproject.toml")
    # README.md
    readme = os.path.join(project_dir, "README.md")
    # setup.cfg
    setup_cfg = os.path.join(project_dir, "setup.cfg")
    # setup.py
    setup_py = os.path.join(project_dir, "setup.py")
    # VERSION
    version = os.path.join(project_dir, "VERSION")
    # gitignore
    gitignore = os.path.join(project_dir, ".gitignore")
    return {"init_py": project_init_py,
            "main_py": project_main_py,
            "tests_init_py": tests_init_py,
            "tests_main_py": tests_main_py,
            "manifest": manifest,
            "pyproject_toml": pyproject_toml,
            "readme": readme,
            "setup_cfg": setup_cfg,
            "setup_py": setup_py,
            "version": version,
            "gitignore": gitignore}


def get_project_name(project_dir=None):
    """
    This function returns the project name.
    Basically it extracts the basename from the path

    [params]
    - project_dir: str, path to the target project

    [returns]
    str, the project name.
    """
    project_dir = project_dir if project_dir else os.getcwd()
    return os.path.basename(project_dir)


def get_pkg_name(project_dir=None):
    """
    This function extracts the application package name from a project_dir.
    Basically it extracts the basename from the path then turns dashes "-" into
    "underscores" "_".

    [params]
    - project_dir: str, path to the target project

    [returns]
    str, the application package name.
    """
    project_dir = project_dir if project_dir else os.getcwd()
    basename = os.path.basename(project_dir)
    cache = basename.split("-")
    pkg_name = "_".join(cache)
    return pkg_name


def _update_setup_cfg(data, project_dir):
    project_name = os.path.basename(project_dir)
    pkg_name = get_pkg_name(project_dir)
    data = data.decode("utf-8")
    data = data.format(project_name=project_name, pkg_name=pkg_name)
    return data.encode("utf-8")
