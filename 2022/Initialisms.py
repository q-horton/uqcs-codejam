#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'InitialismConverter' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def InitialismConverter(s):
    # Write your code here
    arr = s.split()
    res = ""
    for i in arr:
        if i[0].isupper():
            res += i[0]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = InitialismConverter(s)

    fptr.write(result + '\n')

    fptr.close()
