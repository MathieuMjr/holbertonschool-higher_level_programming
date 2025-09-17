#!/usr/bin/python3

"""
This module contains a class representing a rectangle,
its attributes and its methods
"""


class Rectangle:
    """
    This class represent a rectangle
    """

    number_of_instances = 0

    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """
        Initiate an instance with width = 0 and
        height = 0 by default, or given value
        else
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        This function should display the rectangle,
        drawn with #.
        It returns a string so it can be send to
        print.
        """
        res = ""
        if self.height == 0 or self.width == 0:
            return res
        else:
            for ligne in range(0, self.height):
                for element in range(0, self.width):
                    res += "{}".format(self.print_symbol)
                if ligne != self.height - 1:
                    res += '\n'
        return res

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
