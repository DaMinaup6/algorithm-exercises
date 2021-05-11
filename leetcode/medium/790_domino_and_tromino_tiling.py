# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=S-fUTfqrdq8

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0, 0] for _ in range(n + 1)]
        dp[0][0] = dp[1][0] = 1
        for col in range(2, n + 1):
            dp[col][0] = (dp[col - 1][0] + dp[col - 2][0] + 2 * dp[col - 1][1]) % MOD
            dp[col][1] = (dp[col - 2][0] + dp[col - 1][1]) % MOD

        return dp[n][0]

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        prev_dp_1 = prev_dp_2 = [1, 0]
        for col in range(2, n + 1):
            curr_dp = [0, 0]
            curr_dp[0] = (prev_dp_1[0] + prev_dp_2[0] + 2 * prev_dp_1[1]) % MOD
            curr_dp[1] = (prev_dp_2[0] + prev_dp_1[1]) % MOD

            prev_dp_1, prev_dp_2 = curr_dp, prev_dp_1

        return prev_dp_1[0]
