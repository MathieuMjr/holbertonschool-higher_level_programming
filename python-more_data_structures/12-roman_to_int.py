#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    if not roman_string:
        return None
    for i in range(0, len(roman_string)):
        if roman_string[i] == 'I' and i == 0 and i + 1 < len(roman_string):
            number -= 1
        else:
            number += roman[roman_string[i]]
    return number
