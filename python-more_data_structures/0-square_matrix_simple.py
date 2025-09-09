#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        new_matrix.append(list(map(lambda x: x**2, matrix[i])))
        # il faut caster map pour accéder à ses valeurs
    return new_matrix
