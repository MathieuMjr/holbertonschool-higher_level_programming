#!/usr/bin/env python3
"""
This module contains classes that represent Dragons
and creatures capabilities"""


class SwimMixin:
    """
    This mixin class define a creature swimming
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    This mixin class define a creature flying
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    This mixin class define a dragon roaring
    """
    def roar(self):
        print("The dragon roars!")
