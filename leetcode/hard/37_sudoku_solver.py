# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(18 * 9^m)
# Space Complexity: O(m)
# -----------------------------------------
# m := number of blanks in board
# Ref: https://blog.csdn.net/L141210113/article/details/88419719
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board

        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if self.is_valid(i, j) and dfs():
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs()

    def is_valid(self, i, j):
        curr_num = self.board[i][j]
        for index in range(9):
            if index != j and self.board[i][index] == curr_num:
                return False
            if index != i and self.board[index][j] == curr_num:
                return False        
        box_key = (i // 3 * 3, j // 3 * 3)
        for row in range(3):
            for col in range(3):
                if box_key[0] + row != i and box_key[1] + col != j and self.board[box_key[0] + row][box_key[1] + col] == curr_num:
                    return False

        return True
