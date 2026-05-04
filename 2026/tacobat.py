#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tacobat' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING x as parameter.
#

def tacobat(x):
    # Write your code here
    start_point = 0
    end_point = len(x) - 1
    pivot = -1
    while True:
        if x[start_point] != x[end_point]:
            start_point += 1
        else:
            if x[start_point + 1] == x[end_point - 1]:
                pivot = (start_point + end_point) // 2
                break
        if start_point == end_point:
            break
    offset = 0
    while x[pivot - offset] == x[pivot + offset]:
        offset += 1
    return x[pivot - offset] + x[pivot + offset]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    xx = input()

    yy = tacobat(xx)

    fptr.write(yy + '\n')

    fptr.close()
