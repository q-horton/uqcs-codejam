#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unjumble' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING jumbled_text as parameter.
#

def unj_word(word):
    if len(word) <= 3:
        return word
    new_word = []
    wo_hyp = word.split("-")
    for i in range(len(wo_hyp)-1):
        wo_hyp[i] += "-"
    for n in wo_hyp:
        wo_ap = n.split("'")
        for i in range(len(wo_ap)-1):
            wo_ap[i] += "'"
        for j in wo_ap:
            if len(j) <= 3:
                new_word.append(j)
                continue
            k = [len(j)-1, 0]
            for l in range(len(j)):
                if j[l].isalpha() and j[l+1].isalpha():
                    k[0] = l+1
                    break
            for m in range(1, len(j)+1):
                if j[-m].isalpha() and j[-m-1].isalpha():
                    k[1] = -m
                    break
            new_word.append(j[:k[0]])
            new_word.append(j[k[1]-1:k[0]-1:-1])
            new_word.append(j[k[1]:])
    return "".join(new_word)
        

def unjumble(jumbled_text):
    # Write your code here
    new_text = []
    for i in jumbled_text.split():
        new_text.append(unj_word(i))
    return " ".join(new_text)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    jumbled_text = input()

    unjumbled_text = unjumble(jumbled_text)

    fptr.write(unjumbled_text + '\n')

    fptr.close()
