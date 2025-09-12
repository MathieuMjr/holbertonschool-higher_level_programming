#!/usr/bin/python3
"""
5-text_indentation.py

This module contains a fonction that print some text
with 2 newlines after "." ":" and "?" characters
"""


def text_indentation(text):
    """function that print text and 2 newlines after "." ":" and "?" chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char in [".", ":", "?"]:
            print()
            print()
