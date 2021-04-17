# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(start_index, end_index):
            if start_index == end_index:
                return piles[start_index]
            return max(piles[start_index] - dfs(start_index + 1, end_index), piles[end_index] - dfs(start_index, end_index - 1))

        return dfs(0, len(piles) - 1) > 0

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time Complexity: O(n^2)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=xJ1Rc30Pyes

# -----> Version 1: Space Complexity: O(n^2)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for index in range(len(piles)):
            dp[index][index] = piles[index]

        for sub_piles_length in range(2, len(piles) + 1):
            for start_index in range(0, len(piles) - sub_piles_length + 1):
                end_index = start_index + sub_piles_length - 1
                dp[start_index][end_index] = max(piles[start_index] - dp[start_index + 1][end_index], piles[end_index] - dp[start_index][end_index - 1])

        return dp[0][-1] > 0

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [0] * len(piles)
        for sub_piles_length in range(2, len(piles) + 1):
            for start_index in range(0, len(piles) - sub_piles_length + 1):
                end_index = start_index + sub_piles_length - 1
                dp[start_index] = max(piles[start_index] - dp[start_index + 1], piles[end_index] - dp[start_index])

        return dp[0] > 0

# -----------------------------------------
# Model Solution: Math
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/stone-game/solution/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
