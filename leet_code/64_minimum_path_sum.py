# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := number of rows
# n := number of columns
class Solution:
    def minPathSum(self, grid):
        row_num = len(grid)
        col_num = len(grid[0])
        
        dp = [[0 for _ in range(col_num)] for _ in range(row_num)]
        for i in range(row_num):
            for j in range(col_num):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    left_sum = dp[i - 1][j] if i - 1 >= 0 else float('inf')
                    up_sum   = dp[i][j - 1] if j - 1 >= 0 else float('inf')
                    dp[i][j] = grid[i][j] + min(left_sum, up_sum)

        return dp[row_num - 1][col_num - 1]

processor = Solution()
print(f"processor.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])                                                                                                                                                      == 7:  {processor.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7}")
print(f"processor.minPathSum([[1, 2, 3], [4, 5, 6]])                                                                                                                                                                 == 12: {processor.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12}")
print(f"processor.minPathSum([[1, 4, 8, 6, 2, 2, 1, 7], [4, 7, 3, 1, 4, 5, 5, 1], [8, 8, 2, 1, 1, 8, 0, 1], [8, 9, 2, 9, 8, 0, 8, 9], [5, 7, 5, 7, 1, 8, 5, 5], [7, 0, 9, 4, 5, 6, 5, 6], [4, 9, 9, 7, 9, 1, 9, 0]]) == 47: {processor.minPathSum([[1, 4, 8, 6, 2, 2, 1, 7], [4, 7, 3, 1, 4, 5, 5, 1], [8, 8, 2, 1, 1, 8, 0, 1], [8, 9, 2, 9, 8, 0, 8, 9], [5, 7, 5, 7, 1, 8, 5, 5], [7, 0, 9, 4, 5, 6, 5, 6], [4, 9, 9, 7, 9, 1, 9, 0]]) == 47}")
print(f"processor.minPathSum([[7, 4, 8, 7, 9, 3, 7, 5, 0], [1, 8, 2, 2, 7, 1, 4, 5, 7], [4, 6, 4, 7, 7, 4, 8, 2, 1], [1, 9, 6, 9, 8, 2, 9, 7, 2], [5, 5, 7, 5, 8, 7, 9, 1, 4], [0, 7, 9, 9, 1, 5, 3, 9, 4]])         == 50: {processor.minPathSum([[7, 4, 8, 7, 9, 3, 7, 5, 0], [1, 8, 2, 2, 7, 1, 4, 5, 7], [4, 6, 4, 7, 7, 4, 8, 2, 1], [1, 9, 6, 9, 8, 2, 9, 7, 2], [5, 5, 7, 5, 8, 7, 9, 1, 4], [0, 7, 9, 9, 1, 5, 3, 9, 4]]) == 50}")
