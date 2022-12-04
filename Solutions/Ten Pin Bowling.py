#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_CHARACTER_ARRAY turns as parameter.
#

def calculateScore(turns):
    # Write your code here
    scores = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "X": 10, "_": 0}
    tot = 0
    for i in range(0, len(turns)):
        a = turns[i]
        if a[0] == "X" or a[1] == "X":
            if i == len(turns) - 1:
                tot += 10
            else:
                tot += 10 + scores[turns[i+1][0]] + scores[turns[i+1][1]]
        elif a[1] == "/":
            if i == len(turns) - 1:
                tot += 10
            else:
                tot += 10 + scores[turns[i+1][0]]
        else:
            tot += scores[a[0]] + scores[a[1]]
    return tot
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    scores = []

    for _ in range(t):
        scores.append(list(map(lambda x: x[0], input().rstrip().split())))

    total = calculateScore(scores)

    fptr.write(str(total) + '\n')

    fptr.close()
