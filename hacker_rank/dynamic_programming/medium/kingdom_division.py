# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://jimmy-shen.medium.com/kingdom-division-problem-from-hackerrank-e4aa3a8208c8

import math
import os
import random
import re
import sys

from collections import defaultdict, deque

# Complete the kingdomDivision function below.
def kingdomDivision(n, roads): # roads format: [[1, 2], [1, 3], [3, 4], [3, 5]]
    edges  = defaultdict(set)
    degree = defaultdict(int)
    for road in roads:
        city_1, city_2 = road
        edges[city_1].add(city_2)
        edges[city_2].add(city_1)
        degree[city_1] += 1
        degree[city_2] += 1
    
    # The possible divisions for a sub-tree rooted @ node is division[node][parent]
    # where parent = True if the node shares its parent's color
    division = {node: {True: 1, False: 1} for node in degree}
    # We accumulate counts by iteratively stripping leaves from the tree
    leaves = deque([node for node in degree if degree[node] == 1])

    while True:
        node = leaves.popleft()
        # If parent differs, exclude case where ALL children differ
        division[node][False] = division[node][True] - division[node][False]
        # If no edges left, we have reached root and are done
        if degree[node] == 0:
            root = node
            break
        else:
            # Otherwise update parent:
            parent = edges[node].pop()
            # update topology
            edges[parent].discard(node)
            degree[parent] -= 1
            if degree[parent] == 1:
                leaves.append(parent)
            # update counts
            division[parent][True]  *= division[node][True] + division[node][False]
            division[parent][False] *= division[node][False]

    # Note each division has a corresponding one with colors switched
    return 2 * division[root][False] % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()

# -----------------------------------------
# Brute Force
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
# Ref: https://suzyz.github.io/2017/09/08/kingdom-division/
# Note: This approach won't pass test case 11 but it's easier to understand

import math
import os
import random
import re
import sys

from collections import defaultdict
from functools import lru_cache

# Complete the kingdomDivision function below.
def kingdomDivision(n, roads): # roads format: [[1, 2], [1, 3], [3, 4], [3, 5]]
    edges  = defaultdict(set)
    degree = defaultdict(int)
    for road in roads:
        node_1, node_2 = road
        edges[node_1].add(node_2)
        edges[node_2].add(node_1)
        degree[node_1] += 1
        degree[node_2] += 1

    @lru_cache(None)
    def dfs(node, same_as_parent):
        if len(edges[node]) == 0:
            return 1 if same_as_parent else 0

        for child in edges[node]:
            edges[child].discard(node)

        if same_as_parent:
            count = 1
            for child in edges[node]:
                count *= dfs(child, False) + dfs(child, True)
            return count
        else:
            count = 1
            for child in edges[node]:
                count *= dfs(child, False)
            return dfs(node, True) - count

    root = None
    for node in degree:
        if degree[node] == 1:
            root = node
            break

    return 2 * dfs(root, False) % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    sys.setrecursionlimit(2 ** 31 - 1)
    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
