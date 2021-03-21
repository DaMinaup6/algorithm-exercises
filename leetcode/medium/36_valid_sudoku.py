# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rows_valid(board) and self.cols_valid(board) and self.sub_boxes_valid(board)

    def rows_valid(self, board: List[List[str]]) -> bool:
        for row in board:
            nums_set = set()
            for s in row:
                if s.isdigit():
                    if s in nums_set:
                        return False
                    nums_set.add(s)

        return True

    def cols_valid(self, board: List[List[str]]) -> bool:
        for col_idx in range(9):
            nums_set = set()
            for row_idx in range(9):
                s = board[row_idx][col_idx]
                if s.isdigit():
                    if s in nums_set:
                        return False
                    nums_set.add(s)

        return True

    def sub_boxes_valid(self, board: List[List[str]]) -> bool:
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                nums_set = set()
                for i_increment in [0, 1, 2]:
                    for j_increment in [0, 1, 2]:
                        s = board[i + i_increment][j + j_increment]
                        if s.isdigit():
                            if s in nums_set:
                                return False
                            nums_set.add(s)

        return True
