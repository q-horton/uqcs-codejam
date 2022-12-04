#!/bin/python3

import math
import os
import random
import re
import sys

def rail(rails, s):
    # Write your code here
    arr = [""]*rails
    doub = [s[i:i+(rails-1)*2] for i in range(0, len(s), (rails-1)*2)]
    for i in doub:
        for j in range(0, len(i)):
            arr[abs(rails-1-j)] += i[j]
    res = ""
    for k in arr:
        res += k
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input().split("|")

    diff = rail(int(a[0]), a[1])

    fptr.write(str(diff) + '\n')

    fptr.close()