#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Vrbik' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY arr
#

def Vrbik(n, arr):
    # Write your code here
    print(arr)
    output = []
    for i in arr:
        if i[0] >= i[1] and i[0] <= i[2]:
            output.append(i[0])
        else:
            output.append(-1)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    ll = []

    for _ in range(nn):
        ll.append(list(map(int, input().rstrip().split())))

    result = Vrbik(nn, ll)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
