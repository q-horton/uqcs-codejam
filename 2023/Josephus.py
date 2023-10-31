#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'josephus' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def josephus(n, k):
    # Write your code here
    values = list(range(1, n+1))
    index = -1
    while len(values) > 1:
        index = (index + k) % len(values)
        values.pop(index)
        index -= 1
    return values[0]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    nn = int(first_multiple_input[0])

    kk = int(first_multiple_input[1])

    yy = josephus(nn, kk)

    fptr.write(str(yy) + '\n')

    fptr.close()
