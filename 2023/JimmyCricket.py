#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningTeam' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def is_valid_innings(inn):
    balls = inn.split()
    bc = len(balls)
    wc = 0
    is_wc_acc = True
    for i in balls:
        if i == "NB" or i == "WD":
            bc -= 1
        elif i == "X":
            wc += 1
    if wc == 10 and balls[-1] != "X":
        is_wc_acc = False
    return ((bc == 60 or wc == 10) and wc <= 10 and is_wc_acc)
    

def winningTeam(a, b):
    # YOUR SOLUTION HERE
    if is_valid_innings(a) and is_valid_innings(b):
        scores = [0, 0]
        for i in a.split():
            if i == "NB" or i == "WD":
                scores[0] += 1
            elif i.isdigit():
                scores[0] += int(i)
        for i in b.split():
            if i == "NB" or i == "WD":
                scores[1] += 1
            elif i.isdigit():
                scores[1] += int(i)
        if scores[0] == scores[1]:
            return f"Draw: {scores[0]}"
        elif scores[0] > scores[1]:
            return f"Team 1: {scores[0]}"
        elif scores[1] > scores[0]:
            return f"Team 2: {scores[1]}"
    else:
        return "invalid"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = winningTeam(a, b)

    fptr.write(result + '\n')

    fptr.close()
