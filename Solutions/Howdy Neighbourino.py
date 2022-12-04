#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def ending(s):
    # Write your code here
    end = ""
    if s[-1] == ".":
        s = s[:-1]
        end = "."
    if s[-1] == "h":
        return s + "aroo" + end
    elif len(s) > 4 and s[-1] == "r":
        return s + "ino" + end
    elif s[-1] == "d" and s[-3:] != "and":
        return s + "ily-doodily" + end
    elif s[-2:] == "es":
        return s + "ies" + end
    else:
        return s + end

def start(s):
    if s[0] == "d":
        return "diddly ding dong " + s
    elif s[0] == "D":
        return "Diddly ding dong " + s[0].lower() + s[1:]
    elif s[0] == "n":
        return "noodly-" + s
    elif s[0] == "N":
        return "Noodly-" + s[0].lower() + s[1:]
    elif s[0] == "r":
        return "riddly-" + s
    elif s[0] == "R":
        return "Riddly-" + s[0].lower() + s[1:]
    else:
        return s

def word(s):
    if s == "man":
        return "fella"
    elif s == "Man":
        return "Fella"
    elif s == "hello":
        return "howdy"
    elif s == "Hello":
        return "Howdy"
    else:
        return s

def full(s):
    words = s.split()
    new = ""
    for i in words:
        a = word(i)
        b = start(a)
        c = ending(b)
        new += c + " "
    return new[0:-1]

if __name__ == '__main__':
    input_s = input()

    fin = full(input_s)

    print(fin)