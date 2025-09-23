#!/usr/bin/env python3
"""Module for geometric shapes using abstract base classes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, radius):
        """
        Initialize a Circle.

        Args:
            radius (float): The radius of the circle.
        """
        self._radius = radius

    def area(self):
        """Compute the area of the circle."""
        return pi * self._radius ** 2

    def perimeter(self):
        """Compute the perimeter of the circle."""
        return 2 * pi * self._radius


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self._width = width
        self._height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Compute the perimeter of the rectangle."""
        return 2 * (self._width + self._height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object to inspect.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
