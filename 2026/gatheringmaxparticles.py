#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximum_collectable' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER limit
#  2. INTEGER n_spots
#  3. INTEGER_ARRAY particles
#

def get_max_allowed(rem_lim, particles):
    if rem_lim < min(particles.keys()):
        return 0, []
    max_val = 0
    path = []
    for i in particles.keys():
        if i > rem_lim:
            continue
        val = rem_lim - i
        rem_p = particles.copy()
        rem_p[i] -= 1
        if rem_p[i] == 0:
            rem_p.pop(i)
        print(rem_p)
        path_max = get_max_allowed(val, rem_p)
        if path_max[0] + i > max_val:
            max_val = path_max[0] + i
            path = [i] + path_max[1]
    return max_val, path

def maximum_collectable(limit, n_spots, particles):
    # Write your code here
    vals = {}
    for i in particles:
        if i in vals:
            vals[i] += 1
        else:
            vals[i] = 1
    resp = get_max_allowed(limit, vals)
    val = resp[0]
    print(resp[1])
    for i in resp[1]:
        vals[i] -= 1
        if vals[i] == 0:
            vals.pop(i)
    return val + max(vals.keys())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    m = []

    for _ in range(n):
        m_item = int(input().strip())
        m.append(m_item)

    result = maximum_collectable(l, n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
