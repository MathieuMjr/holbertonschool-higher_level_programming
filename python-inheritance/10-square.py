#!/usr/bin/python3
"""
This module contains a subclass that inherit from*
Base Geometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This subclass inherit from Base Geometry
    It represent a Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size,
                                   self.__size)
