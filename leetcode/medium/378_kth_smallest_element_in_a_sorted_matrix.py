# -----------------------------------------
# My Solution: Heap
#
# Time  Complexity: O(klog(n))
# Space Complexity: O(n)
# -----------------------------------------
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row_size = col_size = len(matrix)

        # track elements by storing first row
        # for each iteration find the smallest elment, then add a new index (row_index + 1, col_index) to track_nums
        track_nums = []
        for col_index, cell_value in enumerate(matrix[0]):
            heapq.heappush(track_nums, (cell_value, 0, col_index))

        target_position = (0, 0)
        for _ in range(k)
            _, row_index, col_index = heapq.heappop(track_nums)
            if row_index + 1 < row_size:
                heapq.heappush(track_nums, (matrix[row_index + 1][col_index], row_index + 1, col_index))
            target_position = (row_index, col_index)
        return matrix[target_position[0]][target_position[1]]

# -----------------------------------------
# Model Solution: Heap
#
# Time  Complexity: O(klog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1248424/Python-O(klogk)
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row_size = col_size = len(matrix)

        values_min_heap    = [(matrix[0][0], 0, 0)]
        visited_positions  = set([(0, 0)])
        kth_smallest_value = None
        for _ in range(k):
            kth_smallest_value, row_index, col_index = heapq.heappop(values_min_heap)
            for row_move, col_move in [(1, 0), (0, 1)]:
                next_row_index = row_index + row_move
                next_col_index = col_index + col_move
                if next_row_index == row_size or next_col_index == col_size or (next_row_index, next_col_index) in visited_positions:
                    continue
                heapq.heappush(values_min_heap, (matrix[next_row_index][next_col_index], next_row_index, next_col_index))
                visited_positions.add((next_row_index, next_col_index))

        return kth_smallest_value
