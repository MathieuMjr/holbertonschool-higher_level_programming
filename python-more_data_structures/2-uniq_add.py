#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for nombre in set(my_list):
        res += nombre
    return res

# alternative :
# return sum(set(my_list)
