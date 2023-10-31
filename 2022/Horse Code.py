#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING code
#  2. STRING_ARRAY morse_code
#

def decode(code, morse_code):
    # YOUR CODE
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    horse = {"tbh": "thoroughbred horse", "smh": "shaking my hooves", "gtfo": "galloping through fields occasionally", "idc": "i don't canter", "btw": "big trough of water"}
    arr = code.split("/")
    result = ""
    for i in arr:
        temp = i.split()
        new = ""
        for j in temp:
            new += letters[morse_code.index(j)]
        if new in horse.keys():
            new = horse[new]
        result += new + " "
    return result[0:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    code0 = input()

    morse_code0 = []

    for _ in range(26):
        morse_code0_item = input()
        morse_code0.append(morse_code0_item)

    decoded = decode(code0, morse_code0)

    fptr.write(decoded + '\n')

    fptr.close()
