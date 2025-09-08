#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    return [element if idx == element else my_list[i]
            for i in range(0, len(my_list))]

#    new_list = []
#
#    for i in range(0, len(my_list)):
#        if i != idx:
#            new_list.append(my_list[i])
#        else:
#            new_list.append(element)
#    return new_list
