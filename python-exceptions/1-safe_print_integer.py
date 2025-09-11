#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is not isinstance(value, int) or value is None:
            raise ValueError
        print("{:d}".format(value))
        return True
    except (ValueError, NameError):
        return False
