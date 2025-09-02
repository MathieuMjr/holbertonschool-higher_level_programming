#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        if 'a' <= str[i] <= 'z':
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
    print("")
