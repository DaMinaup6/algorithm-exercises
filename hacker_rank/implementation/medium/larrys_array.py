# -----------------------------------------
# My Solution
#
# Time  Complexity: O(t * n^2)
# Space Complexity: O(n)
# -----------------------------------------
# t := number of test cases

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    num_pos_map = {}
    for index, num in enumerate(A):
        num_pos_map[num] = index
    
    sorted_nums = list(range(1, len(A) + 1))
    for num in sorted_nums:
        target_index = num - 1
        if num_pos_map[num] == target_index:
            continue
        else:
            curr_index = num_pos_map[num]
            if curr_index == 1:
                A[0], A[1], A[2] = A[1], A[2], A[0]
                num_pos_map[A[0]], num_pos_map[A[1]], num_pos_map[A[2]] = 0, 1, 2
                continue

            while curr_index - target_index >= 2:
                A[curr_index - 2], A[curr_index - 1], A[curr_index] = A[curr_index], A[curr_index - 2], A[curr_index - 1]
                num_pos_map[A[curr_index - 2]], num_pos_map[A[curr_index - 1]], num_pos_map[A[curr_index]] = curr_index - 2, curr_index - 1, curr_index
                curr_index -= 2
            if curr_index - target_index == 1:
                if curr_index == len(A) - 1:
                    A[curr_index - 2], A[curr_index - 1], A[curr_index] = A[curr_index - 1], A[curr_index], A[curr_index - 2]
                    num_pos_map[A[curr_index - 2]], num_pos_map[A[curr_index - 1]], num_pos_map[A[curr_index]] = curr_index - 2, curr_index - 1, curr_index
                else:
                    A[curr_index - 1], A[curr_index], A[curr_index + 1] = A[curr_index], A[curr_index + 1], A[curr_index - 1]
                    num_pos_map[A[curr_index - 1]], num_pos_map[A[curr_index]], num_pos_map[A[curr_index + 1]] = curr_index - 1, curr_index, curr_index + 1

    return 'YES' if A == sorted_nums else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
