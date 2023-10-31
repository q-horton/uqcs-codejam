#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abundant_numbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sequence
#

def is_abundant(x):
    factors = []
    for i in range (1, x):
        if x % i == 0:
            factors += [i]
    if sum(factors) > x:
        return True
    return False

def abundant_numbers(n, sequence):
    # Write your code here
    output = []
    for i in sequence:
        if is_abundant(i):
            output += [i]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    qq = list(map(int, input().rstrip().split()))

    result = abundant_numbers(nn, qq)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
