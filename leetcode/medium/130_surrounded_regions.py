# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(board), n := len(board[0])
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    self.spread(board, i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'V' else 'X'

    def spread(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = 'V'

            self.spread(board, i + 1, j)
            self.spread(board, i - 1, j)
            self.spread(board, i, j + 1)
            self.spread(board, i, j - 1)
