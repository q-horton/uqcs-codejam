#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'times_end' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY a as parameter.
#

def times_end(a):
    # Write your code here
    max_sum = 0
    # Rows
    for i in a:
        if max_sum < sum(i):
            max_sum = sum(i)
    # Cols
    for i in range(len(a)):
        col = [a[j][i] for j in range(len(a))]
        if max_sum < sum(col):
            max_sum = sum(col)
    # Diags
    for i in range(len(a)):
        # Top start
        forward = []
        for j in range(len(a) - i):
            forward += [a[j][i + j]]
        rev = []
        for j in range(i):
            rev += [a[j][i - j]]
        if max_sum < max(sum(forward), sum(rev)):
            max_sum = max(sum(forward), sum(rev))
        # Left start
        forward = []
        for j in range(len(a) - i):
            forward += [a[i + j][j]]
        rev = []
        for j in range(i):
            rev += [a[i - j][j]]
        if max_sum < max(sum(forward), sum(rev)):
            max_sum = max(sum(forward), sum(rev))
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa.append(list(map(int, input().rstrip().split())))

    yy = times_end(aa)

    fptr.write(str(yy) + '\n')

    fptr.close()
