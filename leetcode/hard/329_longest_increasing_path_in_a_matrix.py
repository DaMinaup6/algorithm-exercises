# -----------------------------------------
# Model Solution: DFS + Memoization
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82917210
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix  = matrix
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        self.position_longest_path = [[0] * self.col_len for _ in range(self.row_len)]
        
        longest_increasing_path = 1
        for row in range(self.row_len):
            for col in range(self.col_len):
                longest_increasing_path = max(longest_increasing_path, self.longest_increasing_path_from(row, col))
        return longest_increasing_path

    def longest_increasing_path_from(self, row, col):
        if self.position_longest_path[row][col] > 0:
            return self.position_longest_path[row][col]

        longest_increasing_path = 1
        for row_move, col_move in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if self.position_valid(row + row_move, col + col_move) and self.matrix[row][col] < self.matrix[row + row_move][col + col_move]:
                longest_increasing_path = max(longest_increasing_path, 1 + self.longest_increasing_path_from(row + row_move, col + col_move))
        self.position_longest_path[row][col] = longest_increasing_path

        return longest_increasing_path

    def position_valid(self, row, col):
        return 0 <= row < self.row_len and 0 <= col < self.col_len

# -----------------------------------------
# Model Solution: Sort + Dynamic Programming
#
# Time  Complexity: O(mn * log(mn) + 4mn)
# Space Complexity: O(mn)
# -----------------------------------------
# Ref: http://bookshadow.com/weblog/2016/01/20/leetcode-longest-increasing-path-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])

        longest_paths = [[1] * col_len for _ in range(row_len)]
        sorted_matrix = sorted([(row_idx, col_idx, cell_val) for row_idx, row in enumerate(matrix) for col_idx, cell_val in enumerate(row)], key=lambda element: element[2])

        longest_path = 1
        for row_idx, col_idx, cell_val in sorted_matrix:
            for row_idx_move, col_idx_move in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                next_row_idx, next_col_idx = row_idx + row_idx_move, col_idx + col_idx_move
                if 0 <= next_row_idx < row_len and 0 <= next_col_idx < col_len and matrix[row_idx][col_idx] < matrix[next_row_idx][next_col_idx]:
                    longest_paths[next_row_idx][next_col_idx] = max(longest_paths[next_row_idx][next_col_idx], 1 + longest_paths[row_idx][col_idx])
                    longest_path = max(longest_path, longest_paths[next_row_idx][next_col_idx])

        return longest_path
