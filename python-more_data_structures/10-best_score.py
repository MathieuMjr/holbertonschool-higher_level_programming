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
    if name == "":
        return None
    return name

# correction gpt : 
#  if not a_dictionary:  - couvre None et {}
#        return None
#    return max(a_dictionary, key=a_dictionary.get)
