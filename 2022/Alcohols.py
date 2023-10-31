#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'condensedFormula' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING atoms
#  2. INTEGER_ARRAY positions
#

def condensedFormula(atoms, positions):
    # Write your code here
    elements = [0, 0, 0]
    for i in atoms:
        if i == "C":
            elements[0] += 1
        elif i == "H":
            elements[1] += 1
        elif i == "O":
            elements[2] += 1
    for k in positions:
        if k > elements[0]:
            return "invalid"
    if (len(positions) < elements[2]) or (elements[1] != 2 * elements[0] + 2):
        return "invalid"
    else:
        res = ""
        for j in range(0, elements[0]):
            res += "C"
            if j == 0 or j == elements[0]-1:
                if j+1 in positions:
                    res += "H2(OH)"
                else:
                    res += "H3"
            else:
                if j+1 in positions:
                    res += "H(OH)"
                else:
                    res += "H2"
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    atoms = input()

    positions_count = input()

    positions = list(map(int, positions_count.rstrip().split()))

    result = condensedFormula(atoms, positions)

    fptr.write(result + '\n')

    fptr.close()
