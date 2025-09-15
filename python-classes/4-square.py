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
        self.__size = size

    @property
    def size(self):
        """Getter: permet d'accéder à a valeur de __size
        via "size" """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: permet de modifier la valeur de __size
        mais sous certaines conditions ! et via le mot "size"
        et pas __size directement """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcul la surface du carré
        """
        return pow(self.__size, 2)
