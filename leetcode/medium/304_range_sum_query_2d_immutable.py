# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.integral = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.integral[i][j] = matrix[i - 1][j - 1] + self.integral[i - 1][j] + self.integral[i][j - 1] - self.integral[i - 1][j - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.integral[row2 + 1][col2 + 1] - self.integral[row2 + 1][col1] - self.integral[row1][col2 + 1] + self.integral[row1][col1]
