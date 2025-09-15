#!/usr/bin/python3

"""Ce module contient la classe Square qui représente un carré."""


class Square:
    """
    Cette classe représente un carré.

    """

    def __init__(self, size=None):
        """
        Initialise un carré

        Args:
            size (int): Taille du carré.
        """
        if size is None or not isinstance(size, int):
            raise AttributeError("'Square' object has no attribute 'size'")
        self.__size = size
