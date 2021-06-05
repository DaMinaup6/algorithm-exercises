# -----------------------------------------
# My Solution: Prefix Sum
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(mat), n := len(mat[0])
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row_size, col_size = len(mat), len(mat[0])

        prefix_sums = [[0] * (col_size + 1) for _ in range(row_size + 1)]
        for row_index in range(row_size):
            for col_index in range(col_size):
                prefix_sums[row_index + 1][col_index + 1] = mat[row_index][col_index] + prefix_sums[row_index][col_index + 1] + prefix_sums[row_index + 1][col_index] - prefix_sums[row_index][col_index]

        def range_sum(row_index_1, col_index_1, row_index_2, col_index_2):
            return prefix_sums[row_index_2 + 1][col_index_2 + 1] - prefix_sums[row_index_1][col_index_2 + 1] - prefix_sums[row_index_2 + 1][col_index_1] + prefix_sums[row_index_1][col_index_1]

        max_side_length = 0
        for row_index in range(row_size):
            for col_index in range(col_size):
                square_upper_left_position = (row_index - max_side_length, col_index - max_side_length)
                if 0 <= square_upper_left_position[0] < row_size and 0 <= square_upper_left_position[1] < col_size and range_sum(square_upper_left_position[0], square_upper_left_position[1], row_index, col_index) <= threshold:
                    max_side_length += 1
        return max_side_length
