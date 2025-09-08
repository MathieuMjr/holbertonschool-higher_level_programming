#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        # indice -1 car la borne 'stop' est exclue
        print("{:d}".format(my_list[i]))
# alternative donnée par chat gpt :
# for value in reversed(my_list):
#   print("{:d}".format(value))
