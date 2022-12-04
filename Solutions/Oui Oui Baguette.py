#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toText' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

num2word = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "ten-seven", 18: "ten-eight", 19: "ten-nine"}
tens2word = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 8: "four-twenty"}

def toText(n):
    # Write your code here
    res = ""
    if n < 20:
        res = num2word[n]
    elif 20 <= n and n < 60:
        ones = n % 10
        tens = (n - ones) / 10
        if ones == 1:
            res = tens2word[tens] + "-and-" + num2word[ones]
        elif ones == 0:
            res = tens2word[tens]
        else:
            res = tens2word[tens] + "-" + num2word[ones]
    elif 60 <= n and n < 80:
        ones = n - 60
        if ones == 1 or ones == 11:
            res = tens2word[6] + "-and-" + num2word[ones]
        elif ones == 0:
            res = tens2word[6]
        else:
            res = tens2word[6] + "-" + num2word[ones]
    elif n == 80:
        res = "four-twenties"
    elif 80 < n and n < 100:
        ones = n - 80
        res = tens2word[8] + "-" + num2word[ones]
    elif n == 100:
        res = "one-hundred"
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    word = toText(num)

    fptr.write(word + '\n')

    fptr.close()
