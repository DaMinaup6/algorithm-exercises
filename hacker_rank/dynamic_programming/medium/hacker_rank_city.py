# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.hackerrank.com/challenges/hr-city/forum/comments/484584
#!/bin/python3

import os
import sys

#
# Complete the hackerrankCity function below.
#
def hackerrankCity(A):
    MOD = 1000000007

    nodes_count      = [0] * len(A)
    diagonal_length  = [0] * len(A)
    to_junction_sum  = [0] * len(A)
    edges_length_sum = [0] * len(A)
    # initialization
    nodes_count[0]      = 6
    diagonal_length[0]  = 3 * A[0]
    to_junction_sum[0]  = 11 * A[0]
    edges_length_sum[0] = 29 * A[0]

    for index in range(1, len(A)):
        nodes_count[index]      = (nodes_count[index - 1] * 4 + 2) % MOD
        diagonal_length[index]  = (2 * diagonal_length[index - 1] + 3 * A[index]) % MOD
        to_junction_sum[index]  = (4 * to_junction_sum[index - 1] + 3 * A[index] + 2 * diagonal_length[index - 1] + nodes_count[index - 1] * (8 * A[index] + 3 * diagonal_length[index - 1])) % MOD
        edges_length_sum[index] = (A[index] + 4 * edges_length_sum[index - 1] + 8 * to_junction_sum[index - 1] + 12 * A[index] * nodes_count[index - 1] + 12 * nodes_count[index - 1] * to_junction_sum[index - 1] + 16 * A[index] * nodes_count[index - 1] ** 2) % MOD

    return edges_length_sum[len(A) - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()
