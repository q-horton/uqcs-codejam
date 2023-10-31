#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Mocking' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY d
#  3. STRING m
#

def Mocking(n, d, m):
    # Write your code here
    new_str = ""
    for i in range(len(m)):
        flip = False
        for j in d:
            if i % j == 0:
                flip = True
                break
        if flip:
            new_str += m[i].swapcase()
        else:
            new_str += m[i]
    return new_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    aa = list(map(int, input().rstrip().split()))

    s = input()

    result = Mocking(k, aa, s)

    fptr.write(result + '\n')

    fptr.close()
