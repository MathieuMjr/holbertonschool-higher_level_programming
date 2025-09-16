#!/usr/bin/python3

"""
This module contains a class representing a rectangle,
its attributes and its methods
"""


class Rectangle:
    """
    This class represent a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initiate an instance with width = 0 and
        height = 0 by default, or given value
        else
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width value
        Must be a positive int
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height value
        Must be a positive int
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """
        This method returns area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        This method returns perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width
