#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        for i in range(0, x):
            if not isinstance(my_list[i], int):
                continue
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        print("")
        return counter
    except (IndexError, NameError, ValueError):
        # on peut ne mettre que except: raise dans notre cas
        # car le checker n'attends pas d'instruction spécifique
        # selon le type d'erreur mais le comportement naturel de Python
        # ...
        raise
# raise permet d'avoir le résultat du traceback, on dit qu'elle est
# relancée
