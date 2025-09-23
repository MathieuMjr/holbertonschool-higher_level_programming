#!/usr/bin/python3
"""
This module contains a class
"""


class BaseGeometry:
    """
    This is an empty class
    """
    def area(self):
        """
        Function not defined yet
        Raises an execption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that says if a value is an integer.
        Name's just there to be printed in erro message.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This subclass inherit from Base Geometry
    It represent a Rectangle
    """
    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("Height", height):
            self.__height = height
