#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Yelling' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def Yelling(s):
    # Write your code here
    lower = 0
    for i in s:
        if i.islower():
            lower += 1
    length = len(s)
    rat = lower / length
    if rat == 0:
        return "Acceptable."
    elif rat < 0.15:
        return "WHAT WAS THAT?!"
    elif 0.15 <= rat and rat < 0.25:
        return "SAY THAT AGAIN?!"
    elif 0.25 <= rat and rat < 0.5:
        return "YELL IT LOUDER!"
    elif 0.5 <= rat and rat < 0.65:
        return "I CAN'T HEAR YOU!!"
    elif 0.65 <= rat and rat < 0.75:
        return "I THOUGHT I HEARD SOMETHING?!"
    else:
        return "WHY ARE YOU SO QUIET?"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = Yelling(s)

    fptr.write(result + '\n')

    fptr.close()
