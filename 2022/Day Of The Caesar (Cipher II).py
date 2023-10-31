#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesar' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING pt
#

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(n, pt):
    # Write your code here
    res = ""
    for i in pt:
        if i.isalpha():
            if i.isupper():
                res += alpha[(alpha.index(i.lower()) + n) % 26].upper()
            elif i.islower():
                res += alpha[(alpha.index(i) + n) % 26]
        else:
            res += i
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rotation = int(input().strip())

    plaintext = input()

    ciphertext = caesar(rotation, plaintext)

    fptr.write(ciphertext + '\n')

    fptr.close()
