#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
# normalisation, après ça : tuple_a = (a, b, 0 , 0)
# si le tuple n'avait qu'une valeur, alors ça ajoute un 0
# en seconde valeur
# si le tuple n'a aucune valeur, ça ajoute 2 zéro
    tuple_b += (0, 0)
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

# ALTERNATIVES DONNEES PAR CHAT GPT :

# Version compacte avec "normalisation"
# def add_tuple(tuple_a=(), tuple_b=()):
#    a = (tuple_a + (0, 0))[:2]
#    b = (tuple_b + (0, 0))[:2]
#    return (a[0] + b[0], a[1] + b[1])

# Version pythonique avec déballage
# def add_tuple(tuple_a=(), tuple_b=()):
#    (a1, a2) = (tuple_a + (0, 0))[:2]
#    (b1, b2) = (tuple_b + (0, 0))[:2]
#    return (a1 + b1, a2 + b2)
