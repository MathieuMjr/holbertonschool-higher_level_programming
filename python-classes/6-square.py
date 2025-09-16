#!/usr/bin/python3

"""Ce module contient la classe Square qui représente un carré."""


class Square:
    """
    Cette classe représente un carré.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré

        Args:
            size (int): Taille du carré.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter: permet d'accéder à a valeur de __size
        via "size" """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: permet de modifier la valeur de __size
        mais sous certaines conditions ! et via le mot "size"
        et pas __size directement"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter: permet d'accéder à la position du carré
        """
        return self.__position

    @position.setter
    def position(self, coordinates):  # même si +s valeurs, un seul paramètre
        """
        Setter: permet de modifier l'attribut privé selon les conditions fixées
        pour les coordonées/la position du carré
        """
        if not isinstance(coordinates, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(coordinates, tuple):
            if len(coordinates) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            elif not isinstance(coordinates[0], int) or not isinstance(
                coordinates[1], int
            ):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            elif coordinates[0] < 0 or coordinates[1] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

        self.__position = tuple(coordinates)

    def area(self):
        """
        Calcul la surface du carré
        """
        return pow(self.__size, 2)

    def my_print(self):
        """
        Dessine le carré avec des symboles "#" à la position
        donnée à l'objet.
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for space in range(0, self.__position[1]):
                    print()
            for ligne in range(0, self.__size):
                if self.__position[0] > 0:
                    for underscore in range(0, self.__position[0]):
                        print(" ", end="")
                for element in range(0, self.__size):
                    print("#", end="")
                print()
