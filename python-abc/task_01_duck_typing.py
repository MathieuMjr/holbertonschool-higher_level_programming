#!/usr/bin/env python3
"""
This module contains classes related to shapes
Shape is an abstract class with abstract methods
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This class represent a geomtric shape
    Its an abstract class.
    Eache subclass of shape should have
    2 abstract methods : area & perimeter
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This  class represent a circle.
    It has a radius.
    """

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius**2

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    This class represent a rectangle.
    It has a width and a height
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    This function takes an object
    and print its area or a perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
