#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'modular_madness' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER start_value
#  2. LONG_INTEGER modulus
#  3. INTEGER_ARRAY ops
#  4. LONG_INTEGER_ARRAY vals
#

def modular_madness(start_value, modulus, ops, vals):
    # Write your code here
    val = start_value
    for i in range(len(ops)):
        match ops[i]:
            case 1:
                val = (val + (vals[i] % modulus)) % modulus
            case 2:
                val = (val * (vals[i] % modulus)) % modulus
            case 3:
                product = 1
                running_val = val
                temp_val = vals[i] % modulus
                pos = 0
                while temp_val > 0:
                    if temp_val & 1:
                        product = (product * running_val) % modulus                
                    temp_val >>= 1
                    running_val = (running_val ** 2) % modulus
                    pos += 1
                val = product
        print(val)
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    start_value = int(first_multiple_input[0])

    modulus = int(first_multiple_input[1])

    n = int(input().strip())

    ops = list(map(int, input().rstrip().split()))

    vals = list(map(int, input().rstrip().split()))

    result = modular_madness(start_value, modulus, ops, vals)

    fptr.write(str(result) + '\n')

    fptr.close()
