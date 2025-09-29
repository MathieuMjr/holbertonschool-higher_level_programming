#!/usr/bin/python3
"""
This module contains a function that reads files.
"""


def read_file(filename=""):
    """
    Reads the content of a file and print it
    """
    with open(filename, 'r', encoding="utf-8") as file:
        read_file = file.read()
    print(read_file, end="")
