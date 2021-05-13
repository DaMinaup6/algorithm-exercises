# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(mn * maxMove)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(mn * maxMove)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        paths_move_out = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in [0, n - 1]:
                paths_move_out[row][col] += 1
        for row in [0, m - 1]:
            for col in range(n):
                paths_move_out[row][col] += 1

        # dp[i][j][k] := total paths to move to outside boundary starts from (i, j) with maxMove k
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        for move in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    dp[row][col][move] += paths_move_out[row][col]
                    for row_move, col_move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        prev_row = row + row_move
                        prev_col = col + col_move
                        if 0 <= prev_row < m and 0 <= prev_col < n:
                            dp[row][col][move] = (dp[row][col][move] + dp[prev_row][prev_col][move - 1]) % MOD

        return dp[startRow][startColumn][-1]

# -----> Version 2: Space Complexity: O(mn)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        paths_move_out = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in [0, n - 1]:
                paths_move_out[row][col] += 1
        for row in [0, m - 1]:
            for col in range(n):
                paths_move_out[row][col] += 1

        curr_dp = [[0] * n for _ in range(m)]
        for _ in range(maxMove):
            next_dp = [[paths_move_out[row][col] for col in range(n)] for row in range(m)]
            for row in range(m):
                for col in range(n):
                    for row_move, col_move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        prev_row = row + row_move
                        prev_col = col + col_move
                        if 0 <= prev_row < m and 0 <= prev_col < n:
                            next_dp[row][col] = (next_dp[row][col] + curr_dp[prev_row][prev_col]) % MOD
            curr_dp = next_dp

        return curr_dp[startRow][startColumn]
