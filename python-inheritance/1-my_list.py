#!/usr/bin/python3
"""
This module contains a class MyList that inherits from
list
"""


class MyList(list):
    """
    This class inherits from list and contain
    some new methodes compared to list object
    """

    def print_sorted(self):
        """
        This public instance methode prints the list, sorted
        """
        new_list = []
        for element in self:
            new_list.append(element)
        new_list.sort()
        print(new_list)
