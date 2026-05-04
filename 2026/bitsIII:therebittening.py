#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bits_2_electric_boogaloo' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def bits_2_electric_boogaloo(a):
    # Write your code here
    vals = []
    for i in a:
        for j in range(32):
            if (i >> j) & 1 == 0:
                vals += [(i >> j) << j]
                break
    return vals

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa_item = int(input().strip())
        aa.append(aa_item)

    yy = bits_2_electric_boogaloo(aa)

    fptr.write('\n'.join(map(str, yy)))
    fptr.write('\n')

    fptr.close()
