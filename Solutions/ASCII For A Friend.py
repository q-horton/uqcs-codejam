#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ASCIIForAFriend' function below.
#
# The function is expected to return a FLOAT.
# The function accepts STRING s as parameter.
#

def ASCIIForAFriend(s):
    # Write your code here
    tot = 0
    count = 0
    for i in s:
        tot += ord(i)
        count += 1
    return round(tot/count, 2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = ASCIIForAFriend(s)

    fptr.write(str(result) + '\n')

    fptr.close()
