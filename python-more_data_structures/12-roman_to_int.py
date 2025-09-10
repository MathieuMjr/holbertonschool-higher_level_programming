#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    if not roman_string and not isinstance(roman_string, str):
        return None
    for i in range(0, len(roman_string)):
        if roman_string[i] == "I" and (
            i + 1 < len(roman_string)
            and (roman_string[i + 1] == "X" or roman_string[i + 1] == "V")
        ):
            number -= 1
        else:
            number += roman[roman_string[i]]
    return number
