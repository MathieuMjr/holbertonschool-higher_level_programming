#!/usr/bin/python3
"""
This module contains several classes :
- Animal - abstract class that defines
the others.
- Others types of animals that inherits from
Animals attributes
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This class defines what any animal
    can do. For now, just a sound.
    """

    @abstractmethod
    def sound():
        pass


class Dog(Animal):
    """
    This class defines what a dog is and can do.
    Since its an animal, it as sound method.
    Dog's sound is bark, so we defined it
    this way
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This class defines what a cat is and can do.
    It's an animal so just like dog
    it's a subclass of Animal.
    Cat's sound is "Meow".
    """

    def sound(self):
        return "Meow"
