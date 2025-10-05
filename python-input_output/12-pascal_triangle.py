#!/usr/bin/python3
""""
This module contain a function
that compute a pascal triangle
"""


def pascal_triangle(n):
    """
    This function create a list
    of list of a pascal triangle
    """
    my_list = []
    for i in range(1, n + 1):
        new_list = []
        if i <= 2:
            for j in range(0, i):
                new_list.append(1)
            my_list.append(new_list)
        else:
            for j in range(0, i):
                try:
                    if j == 0:
                        new_list.append(1)
                    else:
                        new_list.append(my_list[i - 2][j] +
                                        my_list[i - 2][j - 1])
                except Exception:
                    new_list.append(1)
            my_list.append(new_list)
    return my_list


# correction chat gpt :
# def pascal_triangle(n):
#    triangle = []
#   for i in range(n):
#        row = [1] * (i + 1)
#        for j in range(1, i):
#            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # ③
#        triangle.append(row)
#    return triangle
