#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'MiningCS' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING directions as parameter.
#

def MiningCS(directions):
    # Write your code here
    output = ""
    for i in directions:
        if i.lower() == 'r':
            output += "right\n"
        elif i.lower() == 'l':
            output += "left\n"
        elif i.lower() == 'j':
            output += "jump\n"
        elif i.lower() == 's':
            output += "straight\n"
        else:
            output += "Aaaaah!\n"
    return output[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    result = MiningCS(inp)

    fptr.write(result + '\n')

    fptr.close()
