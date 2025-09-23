#!/usr/bin/python3
"""
This module contains a subclass that inherit from*
Base Geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This subclass inherit from Base Geometry
    It represent a Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] <{}>/<{}>".format(self.__class__.__name__, self.__width,
                                       self.__height)
