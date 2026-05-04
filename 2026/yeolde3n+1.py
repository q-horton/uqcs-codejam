#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ye_olde_3n_plus_1' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY starting_positions as parameter.
#

def ye_olde_3n_plus_1(starting_positions):
    starting_positions.sort()
    # Write your code here
    times = []
    for i in starting_positions:
        pos = i
        steps = 0
        while (pos != 1):
            if pos % 2 == 0:
                pos = pos // 2
            else:
                pos = 3 * pos + 1
            steps += 1
        times += [steps]
    for i in range(len(times)):
        if times[i] == min(times):
            return starting_positions[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    starting_positions = list(map(int, input().rstrip().split()))

    result = ye_olde_3n_plus_1(starting_positions)

    fptr.write(str(result) + '\n')

    fptr.close()
