#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance
of a class that inherited directly or not from a specified class
"""


def inherits_from(obj, a_class):
    """
    This function tells if the object is an instance of a class
    that inherited directly or not from a specified class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        # type(obj) va retourner le nom de la classe de l'objet
        return True
    else:
        return False
