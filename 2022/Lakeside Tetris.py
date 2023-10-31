#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'UQBridges' function below.
#
# The function is expected to return an INTEGER.
#

def UQBridges(a, b):
    # Enter your code here. Use any parameters you wish.
    lake = a.split()
    amp = b.split()
    x1 = int(lake[0]) - int(amp[0])
    x2 = int(amp[0])
    y1 = int(lake[1]) - int(amp[1])
    y2 = int(amp[1])
    if x1 > y1:
        return ((y1+x2)*(y1+y2)-(x2*y2))
    else:
        return ((x1+x2)*(x1+y2)-(x2*y2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    a = input()
    b = input()
    
    result = UQBridges(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
