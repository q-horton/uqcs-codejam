#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'invert_matrix' function below.
#
# The function is expected to return a 2D_FLOAT_ARRAY.
# The function accepts 2D_INTEGER_ARRAY a as parameter.
#

def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]

def pos(val, div):
    if div == 0:
        return 0.0
    else:
        return round(val/div, 2)

def invert_matrix(a):
    # Write your code here
    b = det(a)
    return [[pos(a[1][1],b), pos(-a[0][1],b)], [pos(-a[1][0],b), pos(a[0][0],b)]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    matrix = []

    for _ in range(2):
        matrix.append(list(map(int, input().rstrip().split())))

    result = invert_matrix(matrix)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
