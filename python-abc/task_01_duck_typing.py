#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """This class represents a geometric shape."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """This class represents a circle."""

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return pi * self._radius ** 2

    def perimeter(self):
        return 2 * pi * self._radius

class Rectangle(Shape):
    """This class represents a rectangle."""

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

def shape_info(shape):
    """This function takes a shape object and prints its area and perimeter."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
