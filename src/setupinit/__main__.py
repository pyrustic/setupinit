import os
import os.path
import sys
from setupinit import is_initialized, initialize, get_missing_files


def main():
    project_dir = os.getcwd()
    args = sys.argv[1:]
    if len(args) > 1:
        print(INCORRECT_USAGE)
        return
    if not args:
        print(HELP_TEXT)
        return
    command = args[0].lower()
    if command == "init":
        if is_initialized(project_dir):
            print(ALREADY_INITIALIZED)
        else:
            initialize(project_dir)
            print(SUCCESSFULLY_INITIALIZED)
    elif command == "check":
        check_handler(project_dir)
    elif command in ("--help", "-h"):
        print(HELP_TEXT)
    else:
        print(UNKNOWN_COMMAND)


def check_handler(project_dir):
    missing_files = get_missing_files(project_dir)
    if missing_files:
        print("{}\n".format(NOT_YET_INITIALIZED))
        cache = "  ".join([x for x in missing_files.keys()])
        print("{} ".format(MISSING_FILES), cache)
    else:
        print(ALREADY_INITIALIZED)


HELP_TEXT = """Setupinit - Properly setup Python projects !
https://github.com/pyrustic/setupinit

COMMANDS: 
    init        Initialize the project
    check       Check that the project is initialized"""

ALREADY_INITIALIZED = "This project is already initialized."
NOT_YET_INITIALIZED = "This project isn't yet initialized."
SUCCESSFULLY_INITIALIZED = "Successfully initialized !"
UNKNOWN_COMMAND = "Unknown command."
INCORRECT_USAGE = "Incorrect usage of the command."
MISSING_FILES = "Missing files:"


if __name__ == "__main__":
    main()
