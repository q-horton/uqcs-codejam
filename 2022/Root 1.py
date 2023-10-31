#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'find_min_hp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY rds
#  2. INTEGER b
#

def find_min_hp(rds, b):
    # Write your code here
    max_d = 0
    for i in rds:
        if i > max_d:
            max_d = i
    hp = 0
    b_used = False
    for j in rds:
        if j == max_d and not b_used:
            if max_d > b:
                hp += j - b
                b_used = True
        else:
            hp += j
    return hp + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    buff = int(input().strip())

    num_rounds = int(input().strip())

    round_damages = []

    for _ in range(num_rounds):
        round_damages_item = int(input().strip())
        round_damages.append(round_damages_item)

    min_hp_required = find_min_hp(round_damages, buff)

    fptr.write(str(min_hp_required) + '\n')

    fptr.close()
