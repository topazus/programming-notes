#!/usr/bin/env python


__version__ = "1.0"  # update setup.py when changing this line.
__author__ = "Felix Wang"
__license__ = "MIT"

import argparse
import fnmatch
import logging
import os
import re
import sys


def is_word(s: str) -> bool:
    match = re.search(r"\W", s)
    return match is None


class VariableManipulator(object):
    def __init__(self, val, separator=None) -> None:
        if separator:
            self.separator = separator
        else:
            self.separator = os.pathsep
        self.elements = []
        if val:
            self.elements = [os.path.normpath(x) for x in val.split(self.separator)]

    def get_values(self) -> str:
        return self.separator.join(self.elements)

    def remove_duplicate_paths(self):
        """Removes duplicates in the variable value."""
        unique_path = set()
        filtered_elements = []
        for elem in self.elements:
            if elem.upper() not in unique_path:
                unique_path.add(elem.upper())
                filtered_elements.append(elem)
        self.elements = filtered_elements

    def append_path(self, path) -> None:
        """Appends path at the end of the variable."""
        if not os.path.exists(path):
            logging.warn("invalid path: {}".format(path))
            return
        self.elements.append(path)

    def prepend_path(self, path) -> None:
        """Prepends path at the begining of the variable."""
        if not os.path.exists(path):
            logging.warning("invalid path: {}".format(path))
        self.elements.insert(0, path)

    def remove_path(self, path):
        """Removes specific path."""
        self.elements = [el for el in self.elements if not fnmatch.fnmatch(el, path)]


if __name__ == "__main__":
    # __file__ is the path of this file.
    # os.path.basename(__file__) is the name of this file.
    # os.path.splitext(os.path.basename(__file__)) is a tuple of (name, extension)
    filename, ext = os.path.splitext(os.path.basename(__file__))

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-r",
        "--remove",
        dest="remove",
        action="append",
        metavar="PATH",
        help="remove value(s) from the environment variable.",
    )
    parser.add_argument(
        "-a",
        "--append",
        dest="append",
        action="append",
        metavar="PATH",
        help="append value(s) to the environment variable.",
    )
    parser.add_argument(
        "-p",
        "--prepend",
        dest="prepend",
        action="append",
        metavar="PATH",
        help="prepend value(s) to the environment variable.",
    )
    parser.add_argument(
        "--separator",
        dest="sep",
        metavar="CHAR",
        help="changes the path separator (default is os specific).",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="different output format more readable but invalid. DO NOT ASSIGN to an environment variable.",
    )
    parser.add_argument(
        "variable", help="environment variable or variable value to process."
    )

    arguments = parser.parse_args()

    variable_name = arguments.variable
    value = None  # Could be a variable name.
    if is_word(variable_name):  # If so, converts it to the value.
        value = os.getenv(variable_name)
    manipulator = VariableManipulator(value, separator=arguments.sep)
    if arguments.remove:
        for path in arguments.remove:
            manipulator.remove_path(path)
    if arguments.append:
        for path in arguments.append:
            logging.info("adding {0} to {1}".format(path, manipulator))
            manipulator.append_path(path)
    if arguments.prepend:
        for path in arguments.prepend:
            logging.info("prepending {0} to {1}".format(path, manipulator))
            manipulator.prepend_path(path)
    manipulator.remove_duplicate_paths()
    value = manipulator.get_values()
    output = ""
    if arguments.debug:
        output = "\n".join(manipulator.elements)
    else:
        if sys.platform == "win32":
            output = "set {0}={1}".format(variable_name, value)
        else:
            output = "{0}".format(manipulator.get_values())
    print(output)
