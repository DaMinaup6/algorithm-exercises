# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_area = 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    max_area = max(max_area, dp[i][j])
                elif matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_area = max(max_area, dp[i][j] ** 2)

        return max_area
