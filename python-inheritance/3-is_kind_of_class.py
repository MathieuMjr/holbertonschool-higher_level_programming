#!/usr/bin/python3
"""
This module contains a function that returns True if
an object is an instance of a specific class or of a class that inherited
of this specific class
"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if
    an object is an instance of a specific class or of a class that inherited
    of a this specific class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
