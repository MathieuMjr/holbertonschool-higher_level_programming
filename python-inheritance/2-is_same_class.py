#!/usr/bin/python3

"""This module contains a function that returns
True if object is exactly an instance of the specified class
False otherwise
"""


def is_same_class(obj, a_class):
    """
    This function returns True if obj is an instance
    of a_class.
    False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
