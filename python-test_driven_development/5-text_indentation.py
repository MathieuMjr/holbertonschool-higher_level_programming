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
    counter = 0
    for idx in range(0, len(text)):
        if text[idx] != " ":
            counter = 0
        if text[idx] == " " and counter != 0:
            continue
        print(text[idx], end="")
        if text[idx] in [".", ":", "?"]:
            print()
            print()
            counter += 1
