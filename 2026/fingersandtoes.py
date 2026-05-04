#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fingers_and_toes' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def fingers_and_toes(n):
    # Write your code here
    if n % 20 == 0:
        return f"The whole of the {ORDINALS[n // 20 - 1]} person"
    out_str = ""
    # Remainder
    plural = True
    match (n - 1) % 5:
        case 0:
            out_str += "One"
            plural = False
        case 1:
            out_str += "Two"
        case 2:
            out_str += "Three"
        case 3:
            out_str += "Four"
        case 4:
            out_str += "Five"
    match (n - 1) % 20 // 10:
        case 0:
            out_str += " finger"
        case 1:
            out_str += " toe"
    if plural:
        out_str += "s"
    # Division
    out_str += f" on the {ORDINALS[(n - 1) // 20]} person"
    match (n - 1) % 20 // 5:
        case 1:
            out_str += "'s second hand"
        case 2:
            out_str += "'s first foot"
        case 3:
            out_str += "'s second foot"

    return out_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    yy = fingers_and_toes(nn)

    fptr.write(yy + '\n')

    fptr.close()
