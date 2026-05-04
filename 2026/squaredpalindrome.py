#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squared_palindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER number
#  2. INTEGER bases
#

def squared_palindrome(number, bases):
    # Write your code here
    val = number ** 2
    num_str = ""
    while val != 0:
        unit = val % bases
        val //= bases
        num_str = str(unit) + num_str
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-1 - i]:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    result = squared_palindrome(n, b)

    fptr.write(result + '\n')

    fptr.close()
