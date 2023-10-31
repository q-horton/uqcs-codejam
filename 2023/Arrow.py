#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrow' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts following parameters:
#  1. DOUBLE x
#  2. DOUBLE y
#  3. DOUBLE u
#  4. DOUBLE g
#

def arrow(x, y, u, g):
    # Write your code here
    t1 = math.sqrt(((u**2 - y*g) + math.sqrt((y*g - u**2)**2 - (g**2)*(y**2+x**2)))/((g**2) / 2))
    t2 = math.sqrt(((u**2 - y*g) - math.sqrt((y*g - u**2)**2 - (g**2)*(y**2+x**2)))/((g**2) / 2))
    theta1 = math.atan((y+g*(t1**2)/2)/(x))
    theta2 = math.atan((y+g*(t2**2)/2)/(x))
    if x > 0:
        if theta1 < 0:
            theta1 = 360 + math.degrees(theta1)
        else:
            theta1 = math.degrees(theta1)
        if theta2 < 0:
            theta2 = 360 + math.degrees(theta2)
        else:
            theta2 = math.degrees(theta2)
    else:
        theta1 = 180 + math.degrees(theta1)
        theta2 = 180 + math.degrees(theta2)
    if t1 < t2:
        return [theta1, t1, theta2, t2]
    else:
        return [theta2, t2, theta1, t1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    xx = float(first_multiple_input[0])

    yy = float(first_multiple_input[1])

    uu = float(first_multiple_input[2])

    gg = float(first_multiple_input[3])

    aa = arrow(xx, yy, uu, gg)

    fptr.write('\n'.join(map(str, aa)))
    fptr.write('\n')

    fptr.close()
