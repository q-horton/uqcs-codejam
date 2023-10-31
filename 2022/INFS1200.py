#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insert' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING entry
#  2. STRING_ARRAY data
#

def insert(entry, data):
    # Write your code here
    for i in range(0, len(data)):
        if entry == data[i]:
            return i
        elif entry < data[i]:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    record = input()

    n = int(input().strip())

    records = []

    for _ in range(n):
        records_item = input()
        records.append(records_item)

    index = insert(record, records)

    fptr.write(str(index) + '\n')

    fptr.close()
