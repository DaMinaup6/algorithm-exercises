# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
# n := len(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

# M := number in range [p, q], which means p <= M <= q
# sort arr first, then mini max of M between arr[i - 1] and arr[i] only depends on arr[i - 1] and arr[i]
# e.g. arr == [3, 5, 8, 14] and [p, q] == [4, 9], so for arr[1] and arr[2] we hace
# M == 4 5 6 7 8 9
#    5 1 0 1 2 3 4
#    8 4 3 2 1 0 1
# we can see that mini max between arr[1] and arr[2] equals min(arr[2] - middle_num, middle_num - arr[1]) where middle_num == (arr[2] + arr[1]) // 2
# follow this rule to calculate all mini max between arr[i - 1] and arr[i] to get the answer
def sherlockAndMinimax(arr, p, q):
    arr.sort()
    if arr[-1] <= p:
        return q
    elif arr[0] >= q:
        return p
    arr.append(10 ** 9 + 1) # force calculates the interval between arr[-1] and q if arr[-1] < q

    curr_max_min = -1 if arr[0] <= p else arr[0] - p
    mini_max = p
    for index in range(1, len(arr)):
        prev_num = arr[index - 1]
        curr_num = arr[index]        
        if curr_num <= p or prev_num >= q or curr_num - prev_num == 1:
            continue

        middle_num = (curr_num + prev_num) // 2
        if middle_num < p:
            if curr_num - p > curr_max_min:
                curr_max_min = curr_num - p
                mini_max = p
        elif middle_num > q:
            if q - prev_num > curr_max_min:
                curr_max_min = q - prev_num
                mini_max = q
        elif min(curr_num - middle_num, middle_num - prev_num) > curr_max_min:
            curr_max_min = min(curr_num - middle_num, middle_num - prev_num)
            mini_max = middle_num

    return mini_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pq = input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
