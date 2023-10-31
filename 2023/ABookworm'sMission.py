#!/bin/python3

import math
import os
import random
import re
import sys

def bookworm(book, words):
    code = []
    for i in words:
        page = book[i[0]-1]
        line = page.split("\\n")[i[1]-1]
        word = line.split()[i[2]]
        code.append(word)
    return " ".join(code)

if __name__ == '__main__':
    n = int(input().strip())

    book = []

    for _ in range(n):
        book_item = input()
        book.append(book_item)

    m = int(input().strip())

    words = []

    for _ in range(m):
        words_item = input()
        word_raw = words_item.split()
        word = (int(word_raw[0]), int(word_raw[1]), int(word_raw[2]))
        words.append(word)

    # Write your code here
    print(bookworm(book, words))