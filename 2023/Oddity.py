#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'oddity' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY a as parameter.
#

def oddity(a):
    # Write your code here
    char_app = {}
    for i in a:
        for j in i:
            if not j in char_app:
                char_app[j] = 0
    chars = sorted(list(char_app.keys()))
    for b in chars:
        for c in a:
            if b in c:
                char_app[b] += 1
    output = ""
    for d in chars:
        if char_app[d] % 2 == 1:
            output += d
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa_item = input()
        aa.append(aa_item)

    yy = oddity(aa)

    fptr.write(yy + '\n')

    fptr.close()
