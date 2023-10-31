#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_there_apple' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING message as parameter.
#

def is_there_apple(message):
    # Write your code here
    found = [False] * 5
    for i in message:
        if i.lower() == 'a':
            found[0] = True
        elif i.lower() == 'p' and found[0] and not(found[1]):
            found[1] = True
        elif i.lower() == 'p' and found[1]:
            found[2] = True
        elif i.lower() == 'l' and found[2]:
            found[3] = True
        elif i.lower() == 'e' and found[3]:
            found[4] = True
    if found[4]:
        return "apple that I am going to eat"
    return ""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    reply = is_there_apple(message)

    fptr.write(reply + '\n')

    fptr.close()
