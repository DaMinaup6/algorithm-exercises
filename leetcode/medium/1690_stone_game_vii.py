# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(stones)
# Note: This leads to TLE or MLE
from functools import lru_cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sums = [0]
        for score in stones:
            pre_sums.append(pre_sums[-1] + score)
        def sum_between(i, j):
            return pre_sums[j + 1] - pre_sums[i]

        @lru_cache(None)
        def max_score_diff(start_index, end_index):
            if start_index == end_index:
                return 0

            remove_left_score_diff  = sum_between(start_index + 1, end_index) - max_score_diff(start_index + 1, end_index)
            remove_right_score_diff = sum_between(start_index, end_index - 1) - max_score_diff(start_index, end_index - 1)
            return max(remove_left_score_diff, remove_right_score_diff)
        return max_score_diff(0, len(stones) - 1)

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n^2)
# -----------------------------------------
# n := len(stones)

# -----> Version 1: Space Complexity: O(n^2)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sums = [0]
        for score in stones:
            pre_sums.append(pre_sums[-1] + score)
        def sum_between(i, j):
            return pre_sums[j + 1] - pre_sums[i]

        dp = [[0] * len(stones) for _ in stones]
        for curr_stones_length in range(2, len(stones) + 1):
            for start_index in range(len(stones) - curr_stones_length + 1):
                end_index = start_index + curr_stones_length - 1

                remove_left_score_diff  = sum_between(start_index + 1, end_index) - dp[start_index + 1][end_index]
                remove_right_score_diff = sum_between(start_index, end_index - 1) - dp[start_index][end_index - 1]
                dp[start_index][end_index] = max(remove_left_score_diff, remove_right_score_diff)
        return dp[0][-1]

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sums = [0]
        for score in stones:
            pre_sums.append(pre_sums[-1] + score)
        def sum_between(i, j):
            return pre_sums[j + 1] - pre_sums[i]

        dp = [0] * len(stones)
        for curr_stones_length in range(2, len(stones) + 1):
            for start_index in range(len(stones) - curr_stones_length + 1):
                end_index = start_index + curr_stones_length - 1

                remove_left_score_diff  = sum_between(start_index + 1, end_index) - dp[start_index + 1]
                remove_right_score_diff = sum_between(start_index, end_index - 1) - dp[start_index]
                dp[start_index] = max(remove_left_score_diff, remove_right_score_diff)
        return dp[0]
