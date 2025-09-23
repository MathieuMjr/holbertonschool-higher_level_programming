#!/usr/bin/env python3
"""
This module contains classes related to shapes.
Shape is an abstract class with abstract methods.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This class represents a geometric shape.
    It is an abstract class.
    Each subclass of Shape must implement two abstract methods: area
    and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    This class represents a circle.
    It has a radius.
    """

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return pi * self._radius ** 2

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * pi * self._radius


class Rectangle(Shape):
    """
    This class represents a rectangle.
    It has a width and a height.
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)


def shape_info(shape):
    """
    This function takes a shape object
    and prints its area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
