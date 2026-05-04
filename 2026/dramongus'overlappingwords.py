#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING pattern as parameter.
#

LETTERS = [
0b00000011110111,
0b01001010001111,
0b00000000111001,
0b01001000001111,
0b00000011111001,
0b00000011110001,
0b00000010111101,
0b00000011110110,
0b01001000001001,
0b00000000011110,
0b10010001110000,
0b00000000111000,
0b00010100110110,
0b10000100110110,
0b00000000111111,
0b00000011110011,
0b10000000111111,
0b10000011110011,
0b00000110001101,
0b01001000000001,
0b00000000111110,
0b00110000110000,
0b10100000110110,
0b10110100000000,
0b01010100000000,
0b00110000001001
]

def solve(pattern):
    # Write your code here
    val = int(pattern, 2)
    for _ in pattern:
        for a in range(len(LETTERS)):
            for b in range(len(LETTERS)):
                if a == b:
                    continue
                for c in range(len(LETTERS)):
                    if a == c or b == c:
                        continue
                    for d in range(len(LETTERS)):
                        if a == d or b == d or c == d:
                            continue
                        if LETTERS[a] | LETTERS[b] | LETTERS[c] | LETTERS[d] == val:
                            return f"{chr(ord('A') + a)}{chr(ord('A') + b)}{chr(ord('A') + c)}{chr(ord('A') + d)}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        pattern = input()

        word = solve(pattern)

        fptr.write(word + '\n')

    fptr.close()
