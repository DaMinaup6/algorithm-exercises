# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(board), n := len(board[0])
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        self.board = board

        to_update_cells = []
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                live_neighbors_count = self.calc_live_neighbors(row_idx, col_idx)
                if (live_neighbors_count < 2 or live_neighbors_count > 3) and board[row_idx][col_idx] == 1:
                    to_update_cells.append((row_idx, col_idx, 0))
                elif live_neighbors_count == 3 and board[row_idx][col_idx] == 0:
                    to_update_cells.append((row_idx, col_idx, 1))

        for row_idx, col_idx, new_state in to_update_cells:
            board[row_idx][col_idx] = new_state

    def calc_live_neighbors(self, row_idx, col_idx):
        live_neighbors_count = 0

        for row_move, col_move in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
            curr_row_idx = row_idx + row_move
            curr_col_idx = col_idx + col_move
            if 0 <= curr_row_idx < len(self.board) and 0 <= curr_col_idx < len(self.board[0]):
                cell_val = self.board[curr_row_idx][curr_col_idx]
                live_neighbors_count += (1 if cell_val == 1 else 0)

        return live_neighbors_count

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(board), n := len(board[0])
# Ref:  https://leetcode.com/problems/game-of-life/solution/
# Note: from discussion (https://leetcode.com/problems/game-of-life/solution/330088) the space complexity is not necessarily O(1).
#       If 1 and 0 in board are stored as boolean bit, then it would cause O(32mn) to update them to integer bit
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        self.board = board

        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                live_neighbors_count = self.calc_live_neighbors(row_idx, col_idx)
                if (live_neighbors_count < 2 or live_neighbors_count > 3) and board[row_idx][col_idx] == 1:
                    board[row_idx][col_idx] = -1
                elif live_neighbors_count == 3 and board[row_idx][col_idx] == 0:
                    board[row_idx][col_idx] = 2
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                board[row_idx][col_idx] = (0 if board[row_idx][col_idx] in [-1, 0] else 1)

    def calc_live_neighbors(self, row_idx, col_idx):
        live_neighbors_count = 0

        for row_move, col_move in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
            curr_row_idx = row_idx + row_move
            curr_col_idx = col_idx + col_move
            if 0 <= curr_row_idx < len(self.board) and 0 <= curr_col_idx < len(self.board[0]):
                cell_val = self.board[curr_row_idx][curr_col_idx]
                live_neighbors_count += (1 if abs(cell_val) == 1 else 0)

        return live_neighbors_count
