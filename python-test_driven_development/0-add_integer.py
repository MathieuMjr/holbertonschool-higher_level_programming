#!/usr/bin/python3

"""
0-add_integer.py

This module contains a fonction that add to integers.
Floats can be used and will be typecasted into ints.
"""


def add_integer(a, b=98):
    """add a and b, checking if they are ints or floats"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float) and a >= 10.0**1000:
        raise OverflowError
    else:
        return int(a) + int(b)
