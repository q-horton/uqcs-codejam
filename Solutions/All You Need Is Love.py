#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'AllYouNeedIsLove' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def AllYouNeedIsLove(s):
    # Write your code here
    points = [0, 0]
    games = [0, 0]
    sets = [0, 0]
    for i in s:
        if i == "A":
            points[0] += 1
        elif i == "B":
            points[1] += 1
        
        if (points[0] > 3 and points[0]-points[1] > 1) or points[0] == 7:
            points = [0, 0]
            games[0] += 1
        elif (points[1] > 3 and points[1]-points[0] > 1) or points[1] == 7:
            points = [0, 0]
            games[1] += 1
        
        if games[0] == 6:
            games = [0, 0]
            sets[0] += 1
        elif games[1] == 6:
            games = [0, 0]
            sets[1] += 1
    
    if sets[0] > sets[1]:
        return "A"
    elif sets[1] > sets[0]:
        return "B"
    else:
        if games[0] > games[1]:
            return "A"
        elif games[1] > games[0]:
            return "B"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = AllYouNeedIsLove(s)

    fptr.write(result + '\n')

    fptr.close()
