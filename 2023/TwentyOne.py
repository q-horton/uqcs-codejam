#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'TwentyOne' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sequence as parameter.
#

def TwentyOne(sequence):
    # Write your code here
    cards = sequence.split()
    count = 0
    for i in cards:
        if i in ["T", "J", "Q", "K", "A"]:
            count -= 1
        elif i in ["2", "3", "4", "5", "6"]:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    result = TwentyOne(inp)

    fptr.write(str(result) + '\n')

    fptr.close()
