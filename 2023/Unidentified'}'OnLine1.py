#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'test_if_braces_match' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING braces as parameter.
#

def test_if_braces_match(braces):
    # Write your code here
    counts = [0, 0]
    for i in braces:
        if i == "{":
            counts[0] += 1
        elif i == "}":
            if counts[1] + 1 > counts[0]:
                return 0
            counts[1] += 1
    if counts[0] == counts[1]:
        return 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    braces = input()

    do_braces_match = test_if_braces_match(braces)

    fptr.write(str(do_braces_match) + '\n')

    fptr.close()
