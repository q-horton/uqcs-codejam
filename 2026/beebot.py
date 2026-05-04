#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beebot' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY deliveries
#

def distance(start, dest):
    dist = 0
    diff = [dest[0] - start[0], dest[1] - start[1]]
    if diff[0] != 0 and diff[1] != 0 and (diff[0] / abs(diff[0])) == (diff[1] / abs(diff[1])):
        diag = min(abs(diff[0]), abs(diff[1]))
        dist += int(diag)
        mov = (diff[0] / abs(diff[0])) * diag
        diff[0] -= mov
        diff[1] -= mov
    dist += abs(int(diff[0]))
    dist += abs(int(diff[1]))
    return dist

def beebot(n, deliveries):
    # Write your code here
    order = [(0,0)]
    for i in deliveries:
        order += [(i[0], i[1]), (i[2], i[3])]
    order += [(0,0)]
    tot_energy = 0
    for i in range(len(order) - 1):
        energy = distance(order[i], order[i + 1])
        tot_energy += energy
    return tot_energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    deliveries = []

    for _ in range(n):
        deliveries.append(list(map(int, input().rstrip().split())))

    min_energy = beebot(n, deliveries)

    fptr.write(str(min_energy) + '\n')

    fptr.close()
