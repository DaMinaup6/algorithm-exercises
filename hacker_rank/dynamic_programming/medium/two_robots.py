# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# Ref:
# a) http://blog.pmatias.com/2016/03/14/hackerrank-w19-1/
# b) https://piotr.westfalewicz.com/blog/2016/11/dynamic-programming-in-5-easy-steps-examples-two-robots/
#!/bin/python3

import os
import sys

def twoRobots(m, queries):
    dp = [[float('inf')] * (len(queries) + 1) for _ in range(len(queries) + 1)]
    dp[-1] = [0] * (len(queries) + 1) # base case
    for i in range(len(queries) - 1, 0, -1):
        r1 = queries[i - 1][1]
        q0, q1 = queries[i]
        for j in range(-1, i - 1):
            r2 = queries[j][1] if j >= 0 else q0
            dp[i][j] = abs(q0 - q1) + min(abs(r1 - q0) + dp[i + 1][j], abs(r2 - q0) + dp[i + 1][i - 1])

    return min(dp[1]) + abs(queries[0][0] - queries[0][1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        queries = []

        for _ in range(n):
            queries.append(list(map(int, input().rstrip().split())))

        result = twoRobots(m, queries)

        fptr.write(str(result) + '\n')

    fptr.close()
