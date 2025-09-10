#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for i in range(0, len(roman_string)):
        if roman_string[i] == "I" and (
            i + 1 < len(roman_string)
            and (roman_string[i + 1] == "X" or roman_string[i + 1] == "V")
        ):
            number -= 1
        elif roman_string[i] == "X" and (
            i + 1 < len(roman_string)
            and (roman_string[i + 1] == "C" or roman_string[i + 1] == "L")
        ):
            number -= roman[roman_string[i]]
        elif roman_string[i] == "C" and (
            i + 1 < len(roman_string)
            and (roman_string[i + 1] == "D" or roman_string[i + 1] == "M")
        ):
            number -= roman[roman_string[i]]
        else:
            number += roman[roman_string[i]]
    return number
