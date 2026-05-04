#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'third_base' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def bal_tern_to_int(var):
    dig_val = 1
    sum_val = 0
    for i in range(len(var)):
        match var[-(i+1)]:
            case '1':
                sum_val += dig_val
            case 'T':
                sum_val += -dig_val
        dig_val *= 3
    return sum_val

def int_to_bal_tern(n):
    if n == 0:
        return []
    match n % 3:
        case 0:
            return ['0'] + int_to_bal_tern(n // 3)
        case 1:
            return ['1'] + int_to_bal_tern(n // 3)
        case 2:
            return ['T'] + int_to_bal_tern((n + 1) // 3)

def third_base(a, b):
    # Write your code here
    result = bal_tern_to_int(a) + bal_tern_to_int(b)
    print(int_to_bal_tern(result))
    out_str = "".join(int_to_bal_tern(result)[::-1])
    if out_str == "":
        out_str = "0"
    return out_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = third_base(a, b)

    fptr.write(result + '\n')

    fptr.close()
