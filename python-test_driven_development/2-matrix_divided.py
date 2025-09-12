#!/usr/bin/python3
"""
2-matrix_divided

This module contains a fonction that divide each number in a matrice
by a divider
"""


def matrix_divided(matrix, div):
    """divid each number in a matrice by a divider"""

    row_length = len(matrix[0])
    for ligne in matrix:
        if len(ligne) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for ligne in matrix:
        for valeur in ligne:
            if type(valeur) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for ligne in matrix:
        if not isinstance(ligne, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    new_matrix = []
    for i in range(0, len(matrix)):
        new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[i])))
        # il faut caster map pour accéder à ses valeurs
    return new_matrix
