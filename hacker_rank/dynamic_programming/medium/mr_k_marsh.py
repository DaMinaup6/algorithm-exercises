# -----------------------------------------
# Model Solution
#
# Time  Complexity: O((mn)^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(grid), n := len(grid[0])
# Ref: https://blog.csdn.net/zjucor/article/details/82587399?utm_medium=distribute.pc_relevant.none-task-blog-OPENSEARCH-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-OPENSEARCH-1.control

#!/bin/python3

import os
import sys

#
# Complete the kMarsh function below.
#
def kMarsh(grid):
    up_matrix    = [[0] * len(grid[0]) for _ in range(len(grid))]
    down_matrix  = [[0] * len(grid[0]) for _ in range(len(grid))]
    left_matrix  = [[0] * len(grid[0]) for _ in range(len(grid))]
    right_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        s = 0
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                s += 1
            else:
                s = 0
            left_matrix[i][j] = s
    for i in range(len(grid)):
        s = 0
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == '.':
                s += 1
            else:
                s = 0
            right_matrix[i][j] = s
    for j in range(len(grid[0])):
        s = 0
        for i in range(len(grid)):
            if grid[i][j] == '.':
                s += 1
            else:
                s = 0
            up_matrix[i][j] = s
    for j in range(len(grid[0])):
        s = 0
        for i in range(len(grid) - 1, -1, -1):
            if grid[i][j] == '.':
                s += 1
            else:
                s = 0
            down_matrix[i][j] = s

    max_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'x' or 2 * (down_matrix[i][j] - 1 + right_matrix[i][j] - 1) <= max_perimeter:
                continue

            for p in range(i + down_matrix[i][j] - 1, i, -1):
                if 2 * (p - i + right_matrix[i][j] - 1) <= max_perimeter:
                    continue
                for q in range(j + right_matrix[i][j] - 1, j, -1):
                    if grid[p][q] == 'x' or 2 * (p - i + q - j) <= max_perimeter:
                        continue
                    if up_matrix[p][q] - 1 >= p - i and left_matrix[p][q] - 1 >= q - j:
                        max_perimeter = max(max_perimeter, 2 * (p - i + q - j))

    return max_perimeter if max_perimeter > 0 else 'impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    grid = []

    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)

    result = kMarsh(grid)
    fptr.write(str(result) + '\n')
    fptr.close()
