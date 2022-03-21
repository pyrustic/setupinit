import os
import os.path
import sys
from setupinit import initialized, initialize, get_missing_files


def main():
    project_dir = os.getcwd()
    args = sys.argv[1:]
    if len(args) > 1:
        print("Incorrect usage of this command")
        return
    if not args:
        print_help()
        return
    command = args[0]
    if command == "init":
        if initialized(project_dir):
            print("This project is already initialized.")
        else:
            initialize(project_dir)
            print("Successfully initialized !")
    elif command == "check":
        check_handler(project_dir)
    elif command == "help":
        print_help()
    else:
        print("Unknown command.")


def check_handler(project_dir):
    missing_files = get_missing_files(project_dir)
    if missing_files:
        print("\nThis project isn't yet initalized.\n")
        cache = "  ".join([x for x in missing_files.keys()])
        print("Missing files: ", cache)
    else:
        print("This project is already initialized !")


def print_help():
    print("\nWelcome to Setupinit !")
    print("The tool to quickly setup a Python project !")
    print("https://github.com/pyrustic/setupinit")
    print("\nThis project is part of the Pyrustic Open Ecosystem")
    print("https://pyrustic.github.io")
    print("\nCommands: init  check  help")


if __name__ == "__main__":
    main()
