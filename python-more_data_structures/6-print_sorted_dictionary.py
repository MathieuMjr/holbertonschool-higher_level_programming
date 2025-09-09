#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))

# alternative :
# for key in sorted(a_dictionary):
#    print("{}: {}".format(key, a_dictionary[key]))
# tuples are not used this time, so no need to .items
