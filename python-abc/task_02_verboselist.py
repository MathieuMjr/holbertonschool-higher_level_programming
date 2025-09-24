#!/usr/bin/env python3
"""
This module contain a custom version
of list that print what some methods
just did.
"""


class VerboseList(list):
    """
    Customized list class with prints
    on some methods :
    - append
    - remove
    - extend
    - pop
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        valeur = super().pop(index)
        print(f"Popped [{valeur}] from the list.")
        return valeur
