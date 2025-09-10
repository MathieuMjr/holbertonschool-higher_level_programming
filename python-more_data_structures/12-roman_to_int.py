#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    if not roman_string:
        return None
    for char in roman_string:
        if roman.get(char, 0) != 0:
            number += roman[char]
    return number
