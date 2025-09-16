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
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__height = value
