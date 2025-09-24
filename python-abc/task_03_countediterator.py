#!/usr/bin/env python3
"""
CountedIterator module.

Defines CountedIterator, an iterator that wraps any iterable
and counts how many elements have been iterated so far.
"""


class CountedIterator:
    """Iterator that counts the number of elements returned."""

    def __init__(self, iterable):
        self.iter_object = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the number of elements already iterated."""
        return self.counter

    def __next__(self):
        """Return the next element and increment the counter; raises
        StopIteration when exhausted."""
        try:
            self.counter += 1
            item = next(self.iter_object)
            return item
        except StopIteration:
            raise
