#!/bin/python3

import math
import os
import random
import re
import sys

r = 3.7783

def rng(x0, mi, ma, n):
    x = [0]*(n+1)
    x[0] = x0
    for i in range(1, n+1):
        x[i] = r*x[i-1]*(1-x[i-1])
    for j in range(0, len(x)):
        x[j] = mi + x[j]*(ma-mi)
    return x[1:]
    

if __name__ == '__main__':
    a = input().split()

    fin = rng(float(a[0]), int(a[1]), int(a[2]), int(a[3]))
    for i in fin:
        print(round(i, 5))