# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(rc * log(rc))
# Space Complexity: O(rc)
# -----------------------------------------
# r := len(matrix), c := len(matrix[0])
#
# Question: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
# Ref: https://cp-wiki.vercel.app/tutorial/kick-start/2021A/#problem-c-rabbit-house

import heapq

def update_value_at(matrix, i, j, val):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and val > matrix[i][j]:
        matrix[i][j] = val
        return True
    return False

def calc_boxes(matrix):
    curr_sum = 0
    max_heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            curr_sum += matrix[i][j]
            heapq.heappush(max_heap, (-matrix[i][j], i, j))

    while len(max_heap) > 0:
        height, i, j = heapq.heappop(max_heap)
        height *= -1
        if update_value_at(matrix, i - 1, j, height - 1):
            heapq.heappush(max_heap, (1 - height, i - 1, j))
        if update_value_at(matrix, i + 1, j, height - 1):
            heapq.heappush(max_heap, (1 - height, i + 1, j))
        if update_value_at(matrix, i, j - 1, height - 1):
            heapq.heappush(max_heap, (1 - height, i, j - 1))
        if update_value_at(matrix, i, j + 1, height - 1):
            heapq.heappush(max_heap, (1 - height, i, j + 1))

    new_sum = sum([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))])
    return new_sum - curr_sum

t = int(input())
for i in range(1, t + 1):
    rows, cols = [int(s) for s in input().split(" ")]
    matrix = []
    for _ in range(rows):
        matrix.append([int(s) for s in input().split(" ")])

    print("Case #{}: {}".format(i, calc_boxes(matrix)))
