#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY birthdays
#

def solve(n, birthdays):
    # YOUR SOLUTION
    arr = [0] * 365
    for i in birthdays:
        arr[i] += 1
    bottom = n
    index = 0
    for j in range(0, len(arr)):
        if arr[j] < bottom:
            bottom = arr[j]
            index = j
    return index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n0 = int(input().strip())

    birthdays0 = []

    for _ in range(n0):
        birthdays0_item = int(input().strip())
        birthdays0.append(birthdays0_item)

    day = solve(n0, birthdays0)

    fptr.write(str(day) + '\n')

    fptr.close()
