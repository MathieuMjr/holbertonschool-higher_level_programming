#!/usr/bin/python3

"""Ce module contient la classe Square qui représente un carré."""


class Square:
    """
    Cette classe représente un carré.

    """

    def __init__(self, size=0):
        """
        Initialise un carré

        Args:
            size (int): Taille du carré.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
