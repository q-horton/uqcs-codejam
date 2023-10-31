#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def maxLoss(prices):
    # Write your code here
    diff = 0
    for i in range(0,len(prices)):
        a = prices[i]
        for j in range(i+1,len(prices)):
            b = prices[j]
            if (a-b) > diff:
                diff = a-b
    return diff
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    diff = maxLoss(p)

    fptr.write(str(diff) + '\n')

    fptr.close()
