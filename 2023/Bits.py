#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bits' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def bits(a):
    # Write your code here
    output = []
    for i in a:
        if i >= 0:
            ubin = bin(i)
            tcbin = ["0"]*(34-len(ubin)) + list(ubin[2:])
        else:
            ubin = bin(i + 1)
            tcbin = ["0"]*(35-len(ubin)) + list(ubin[3:])
            for j in range(len(tcbin)):
                if tcbin[j] == "0":
                    tcbin[j] = "1"
                else:
                    tcbin[j] = "0"
        print(tcbin)
        for k in range(1, len(tcbin)+1):
            if tcbin[-k] == "1":
                tcbin[-k] = "0"
                break
        print(tcbin)
        if tcbin[0] == "1":
            for l in range(len(tcbin)):
                if tcbin[l] == "0":
                    tcbin[l] = "1"
                else:
                    tcbin[l] = "0"
            tcbin.insert(0, "-")
        outstr = "".join(tcbin)
        outval = int(outstr, 2)
        if outstr[0] == "-":
            outval -= 1
        output.append(outval)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa_item = int(input().strip())
        aa.append(aa_item)

    yy = bits(aa)

    fptr.write('\n'.join(map(str, yy)))
    fptr.write('\n')

    fptr.close()
