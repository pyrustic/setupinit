import os
import os.path
import pkgutil


def initialized(project_dir=None):
    """
    Check if a Python project is initialized.
    This function checks the files present in the root against a list of
    required filenames (see the function: get_required_filenames())

    [parameters]
    - project_dir: str, the path to the project root.
    If you don't set a path, the value of 'os.getcwd()' will be used

    [return]
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

    [parameters]
    - project_dir: str, the path to the project root. By default, os.getcwd is called

    [return]
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

    [parameters]
    - project_dir: str, the path to the project root. By default, os.getcwd is called
    """
    if not project_dir:
        project_dir = os.getcwd()
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
        elif key == "manifest":
            data = _update_manifest(data, project_dir)
        with open(filename, "wb") as file:
            file.write(data)


def get_required_filenames(project_dir=None):
    """Returns a dict of required filenames.

    [parameters]
    - project_dir: str, the path to the project root. By default, os.getcwd is called

    [return]
    Returns a dict.
    The keys of the dict are the canonical names of the required files.
    The values are filenames as they should be if these files exist.
    Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}
    """
    if not project_dir:
        project_dir = os.getcwd()
    # app_pkg
    app_pkg = get_app_pkg(project_dir)
    app_dir = os.path.join(project_dir, app_pkg)
    app_init = os.path.join(app_dir, "__init__.py")
    app_main = os.path.join(app_dir, "__main__.py")
    # tests
    tests = os.path.join(project_dir, "tests")
    tests_init = os.path.join(tests, "__init__.py")
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
    return {"app_init": app_init, "app_main": app_main,
            "tests_init": tests_init, "manifest": manifest,
            "pyproject_toml": pyproject_toml, "readme": readme,
            "setup_cfg": setup_cfg, "setup_py": setup_py,
            "version": version, "gitignore": gitignore}


def get_project_name(project_dir=None):
    """
    This function returns the project name.
    Basically it extracts the basename from the path

    [parameters]
    - project_dir: str, path to the target project

    [return]
    str, the project name.
    """
    if not project_dir:
        project_dir = os.getcwd()
    return os.path.basename(project_dir)


def get_app_pkg(project_dir=None):
    """
    This function extracts the application package name from a project_dir.
    Basically it extracts the basename from the path then turns dashes "-" into
    "underscores" "_".

    [parameters]
    - project_dir: str, path to the target project

    [return]
    str, the application package name.
    """
    if not project_dir:
        project_dir = os.getcwd()
    basename = os.path.basename(project_dir)
    cache = basename.split("-")
    app_pkg = "_".join(cache)
    return app_pkg


def _update_setup_cfg(data, project_dir):
    project_name = os.path.basename(project_dir)
    app_pkg = get_app_pkg(project_dir)
    data = data.decode("utf-8")
    data = data.format(project_name=project_name, app_pkg=app_pkg)
    return data.encode("utf-8")


def _update_manifest(data, project_dir):
    app_pkg = get_app_pkg(project_dir)
    data = data.decode("utf-8")
    data = data.format(app_pkg=app_pkg)
    return data.encode("utf-8")
