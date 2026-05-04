#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sponsorship' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#

def sponsorship(b):
    # Write your code here
    c = set(b)
    max_income = 0
    value = 0
    for i in c:
        count = 0
        for j in b:
            if j >= i:
                count += 1
        if max_income < count * i:
            max_income = count * i
            value = i
    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    bb = []

    for _ in range(nn):
        bb_item = int(input().strip())
        bb.append(bb_item)

    yy = sponsorship(bb)

    fptr.write(str(yy) + '\n')

    fptr.close()
