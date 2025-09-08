#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return (new_string)

# alternative chat gpt :
# def no_c(my_string):
#   return "".join([char for char in my_string if char not in ('c', 'C')])
