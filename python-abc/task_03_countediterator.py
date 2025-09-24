#!/usr/bin/env python3
"""
CountedIterator module.

Defines CountedIterator, an iterator that wraps any iterable
and counts how many elements have been iterated so far.
"""


class CountedIterator:
    """Iterator that counts the number of elements returned."""

    def __init__(self, iterable):
        self.__iter_object = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """Return the number of elements already iterated."""
        return self.__counter

    def __next__(self):
        """Return the next element and increment the counter; raises
        StopIteration when exhausted."""
        self.__counter += 1
        item = next(self.__iter_object)
        return item
