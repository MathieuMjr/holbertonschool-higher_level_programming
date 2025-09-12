#!/usr/bin/python3
"""
4-print_square.py

This module contains a fonction that print a square of a specific
size with #
"""


def print_square(size):
    """This function print a square of # of the size you want"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for ligne in range(0, size):
        for element in range(0, size):
            print("#", end="")
        print()
