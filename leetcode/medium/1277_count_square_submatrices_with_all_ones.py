# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])
        def value_at(i, j):
            return matrix[i][j] if 0 <= i < row_len and 0 <= j < col_len else 0

        number_of_squares = 0
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] != 0:
                    curr_val = 1 + min(value_at(i - 1, j), value_at(i, j - 1), value_at(i - 1, j - 1))
                    matrix[i][j] = curr_val
                    number_of_squares += curr_val

        return number_of_squares
