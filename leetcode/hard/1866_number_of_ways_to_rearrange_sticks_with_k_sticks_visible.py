# -----------------------------------------
# Model Solution
#
# Time Complexity: O(kn)
# -----------------------------------------
# Ref: https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/discuss/1211169/JavaC++Python-Concise-DP-Solution/938375

# -----> Version 1: Space Complexity: O(kn)
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 1
        for sticks_count in range(2, n + 1):
            for visible_sticks_count in range(1, k + 1):
                dp[sticks_count][visible_sticks_count] = (dp[sticks_count - 1][visible_sticks_count - 1] + dp[sticks_count - 1][visible_sticks_count] * (sticks_count - 1)) % MOD
        return dp[-1][-1]

# -----> Version 2: Space Complexity: O(k)
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        curr_dp = [0] * (k + 1)
        curr_dp[1] = 1
        for sticks_count in range(2, n + 1):
            next_dp = [0] * (k + 1)
            for visible_sticks_count in range(1, k + 1):
                next_dp[visible_sticks_count] = (curr_dp[visible_sticks_count - 1] + curr_dp[visible_sticks_count] * (sticks_count - 1)) % MOD
            curr_dp = next_dp
        return curr_dp[-1]
