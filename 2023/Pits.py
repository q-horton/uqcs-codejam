#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def pits(grid):
    # Write your code here
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if x > 0:
                if grid[x][y] >= grid[x-1][y]:
                    continue
            if x < len(grid)-1:
                if grid[x][y] >= grid[x+1][y]:
                    continue
            if y > 0:
                if grid[x][y] >= grid[x][y-1]:
                    continue
            if y < len(grid[x])-1:
                if grid[x][y] >= grid[x][y+1]:
                    continue
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    mm = int(first_multiple_input[0])

    nn = int(first_multiple_input[1])

    gg = []

    for _ in range(mm):
        gg.append(list(map(int, input().rstrip().split())))

    yy = pits(gg)

    fptr.write(str(yy) + '\n')

    fptr.close()
