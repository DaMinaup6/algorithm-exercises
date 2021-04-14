# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        move_change_mapping = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        spiral_order = []

        curr_move = (0, 1)
        row_idx = col_idx = 0
        while len(spiral_order) < row_len * col_len:
            spiral_order.append(matrix[row_idx][col_idx])
            matrix[row_idx][col_idx] = None

            next_row_idx = row_idx + curr_move[0]
            next_col_idx = col_idx + curr_move[1]
            if 0 <= next_row_idx < row_len and 0 <= next_col_idx < col_len and matrix[next_row_idx][next_col_idx] is not None:
                row_idx = next_row_idx
                col_idx = next_col_idx
            else:
                curr_move = move_change_mapping[curr_move]
                row_idx += curr_move[0]
                col_idx += curr_move[1]

        return spiral_order
