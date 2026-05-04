#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'scared_weird_little_guys' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING x as parameter.
#

def scared_weird_little_guys(x):
    words = x.split(' ')
    longest_word = max([len(i) for i in words])
    result = ""
    left = True
    for i in words:
        if left:
            result += i + " "*(longest_word - len(i) + 1) + "\n"
        else:
            result += " "*(longest_word - len(i) + 1) + i + "\n"
        left = not left
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    xx = input()

    yy = scared_weird_little_guys(xx)

    fptr.write(yy + '\n')

    fptr.close()
