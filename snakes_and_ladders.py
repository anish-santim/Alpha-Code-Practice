

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    ladders_map = collections.defaultdict(lambda: -1)
    snakes_map = collections.defaultdict(lambda: -1)

    for [pos1, pos2] in ladders: ladders_map[pos1] = pos2
    for [pos1, pos2] in snakes: snakes_map[pos1] = pos2

    deque = collections.deque([(1, 0)])
    visited_node = set([1])

    while deque:
        (curr_pos, curr_level) = deque.popleft()

        if curr_pos==100: return curr_level

        for step in range(1, 7):
            next_pos = (curr_pos+step)
            if next_pos not in visited_node:
                if snakes_map[next_pos]!=-1: next_pos = snakes_map[next_pos]
                if ladders_map[next_pos]!=-1: next_pos = ladders_map[next_pos]
                deque.append((next_pos, t+1))
                visited_node.add(next_pos)
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
