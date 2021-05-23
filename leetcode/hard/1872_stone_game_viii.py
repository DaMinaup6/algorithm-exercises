# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre_sums = [0]
        for index in range(len(stones)):
            pre_sums.append(pre_sums[-1] + stones[index])

        @lru_cache(None)
        # dfs := max score current player can get - max score next player can get
        def dfs(curr_index):
            if curr_index == len(stones) - 1:
                return 0

            score = -float('inf')
            # need select at least two piles, so next_index starts from curr_index + 1
            for next_index in range(curr_index + 1, len(stones)):
                # e.g. stones == [-10, -12, -10, -12]
                # If Alice selects first two piles, which means curr_index stops at index 1, she gets score -10 + (-12) == -22
                # In next step, Bob starts from curr_index + 1, which is 2.
                # If Bob select first two piles only, he gets score -22 + (-10) == (-10 + (-12)) + (-10) == pre_sums[2 + 1] == pre_sums[3],
                # that's why we don't need to consider something like pre_sums[next_index + 1] - pre_sums[curr_index] since no matter which pile we choose,
                # the score equals stones[0] + stones[1] + ... + stones[next_index]
                score = max(score, pre_sums[next_index + 1] - dfs(next_index))
            return score
        return max(dfs(0), pre_sums[len(stones)])

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre_sums = [0]
        for index in range(len(stones)):
            pre_sums.append(pre_sums[-1] + stones[index])

        dp = [-float('inf')] * len(stones)
        dp[-1] = 0
        dp[-2] = pre_sums[len(stones)]
        for curr_index in range(len(stones) - 3, -1, -1):
            # If we transfer DFS to DP then it would looks like this
            #
            # score = -float('inf')
            # for next_index in range(curr_index + 1, len(stones)):
            #     score = max(score, pre_sums[next_index + 1] - dp[next_index])
            # dp[curr_index] = score
            #
            # which means for dp[curr_index],     its value is max value from                                            pre_sums[curr_index + 2] - dp[curr_index + 1], ..., pre_sums[len(stones)] - dp[len(stones) - 1]
            #             for dp[curr_index - 1], its value is max value from pre_sums[curr_index + 2] - dp[curr_index], pre_sums[curr_index + 2] - dp[curr_index + 1], ..., pre_sums[len(stones)] - dp[len(stones) - 1]
            # ...
            # notice that for dp[curr_index - 1], we already know the max value from pre_sums[curr_index + 2] - dp[curr_index + 1] to pre_sums[len(stones)] - dp[len(stones) - 1] since it's been
            # calculated and stored in dp[curr_index], so for dp[curr_index - 1] its value would be max(pre_sums[curr_index + 2] - dp[curr_index], dp[curr_index])
            dp[curr_index] = max(pre_sums[curr_index + 2] - dp[curr_index + 1], dp[curr_index + 1])
        return dp[0]

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre_sum = sum(stones)

        dp = pre_sum
        pre_sum -= stones[-1]
        for index in range(len(stones) - 3, -1, -1):
            dp = max(pre_sum - dp, dp)
            # previously pre_sums equals sum(stones[:(len(stones) - 1)]), sum(stones[:(len(stones) - 2)]), ...
            # which equals (stones[0] + ... + stones[len(stones) - 2]), (stones[0] + ... + stones[len(stones) - 3]), ...
            # so here use index + 1 since len(stones) - 3 + 1 == len(stones) - 2, len(stones) - 4 + 1 == len(stones) - 3, ...
            pre_sum -= stones[index + 1]
        return dp
