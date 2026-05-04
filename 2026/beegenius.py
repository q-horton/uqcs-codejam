#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'beebot' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY deliveries
#

def distance(start, dest):
    dist = 0
    diff = [dest[0] - start[0], dest[1] - start[1]]
    if diff[0] != 0 and diff[1] != 0 and (diff[0] / abs(diff[0])) == (diff[1] / abs(diff[1])):
        diag = min(abs(diff[0]), abs(diff[1]))
        dist += int(diag)
        mov = (diff[0] / abs(diff[0])) * diag
        diff[0] -= mov
        diff[1] -= mov
    dist += abs(int(diff[0]))
    dist += abs(int(diff[1]))
    return dist

def pathing(energies):
    frontier = []
    for k, v in energies[-1].items():
        heapq.heappush(frontier, (v, k))
    explored = set()
    path = [-1]
    while True:
        weight, dest = heapq.heappop(frontier)
        if dest in explored:
            continue
        path.append(dest)
        print(path, explored)
        if dest == -1:
            break
        explored.add(dest)
        for k, v in energies[dest].items():
            if k in explored:
                continue
            heapq.heappush(frontier, (v + weight, k))
        print(frontier)
    print(path)
    return path
        

def beebot(n, deliveries):
    # Write your code here
    order = []
    for i in deliveries:
        start = (i[0], i[1])
        end = (i[2], i[3])
        order += [(start, end, distance(start, end))]
    path_energies = {-1: {}}
    for i in range(len(order)):
        path_energies[-1][i] = distance((0,0), order[i][0])
        path_energies[i] = {-1: distance(order[i][1], (0,0))}
        for j in range(len(order)):
            if i == j:
                continue
            path_energies[i][j] = distance(order[i][1], order[j][0])
    print(path_energies)
    path = pathing(path_energies)
    tot_energy = 0
    for i in range(len(path) - 1):
        print(f"{path[i]} to {path[i + 1]} is {path_energies[path[i]][path[i + 1]]}")
        print(f"{path[i + 1]} is {order[path[i + 1]][2]}")
        tot_energy += path_energies[path[i]][path[i + 1]]
        if path[i + 1] != -1:
            tot_energy += order[path[i + 1]][2]
    return tot_energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    deliveries = []

    for _ in range(n):
        deliveries.append(list(map(int, input().rstrip().split())))

    min_energy = beebot(n, deliveries)

    fptr.write(str(min_energy) + '\n')

    fptr.close()
