#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    max = 0
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
            name = key
            return name
