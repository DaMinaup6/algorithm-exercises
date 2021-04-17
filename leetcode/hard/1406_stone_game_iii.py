# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dfs(start_index):
            if start_index == len(stoneValue):
                return 0
            if start_index == len(stoneValue) - 1:
                return stoneValue[start_index]
            if start_index == len(stoneValue) - 2:
                return max(stoneValue[start_index] - stoneValue[start_index + 1], stoneValue[start_index] + stoneValue[start_index + 1])
            
            # Note: without loss of generality, suppose current player is Alice
            # e.g. take the first term for example
            # stoneValue[start_index] == First stone value
            # dfs(start_index + 1)    == Score of Bob can get from remaining values minus score of Alice can get from remaining values
            # so stoneValue[start_index] - dfs(start_index + 1) == (First stone value + score of Alice can get from remaining values) - Score of Bob can get from remaining values
            # then the result would be maximum score Alice can get - maximum score Bob can get
            return max(stoneValue[start_index] - dfs(start_index + 1), stoneValue[start_index] + stoneValue[start_index + 1] - dfs(start_index + 2), stoneValue[start_index] + stoneValue[start_index + 1] + stoneValue[start_index + 2] - dfs(start_index + 3))

        alice_score_minus_bob_score = dfs(0)
        if alice_score_minus_bob_score == 0:
            return 'Tie'
        return 'Alice' if alice_score_minus_bob_score > 0 else 'Bob'

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        max_relative_score = [-float('inf')] * (len(stoneValue) + 1) # max score of Alice can get - max score of Bob can get
        max_relative_score[-1] = 0
        max_relative_score[-2] = stoneValue[-1]
        if len(stoneValue) >= 2:
            max_relative_score[-3] = max(stoneValue[-2] - stoneValue[-1], stoneValue[-2] + stoneValue[-1])
        for index in range(len(stoneValue) - 3, -1, -1):
            max_relative_score[index] = max(sum(stoneValue[index:(index + picked_stone_count)]) - max_relative_score[index + picked_stone_count] for picked_stone_count in [1, 2, 3])

        if max_relative_score[0] == 0:
            return 'Tie'
        return 'Alice' if max_relative_score[0] > 0 else 'Bob'

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        max_relative_scores = [stoneValue[-1], 0] # max score of Alice can get - max score of Bob can get
        if len(stoneValue) >= 2:
            max_relative_scores.insert(0, max(stoneValue[-2] - stoneValue[-1], stoneValue[-2] + stoneValue[-1]))
        for index in range(len(stoneValue) - 3, -1, -1):
            curr_max_relative_score = max(sum(stoneValue[index:(index + picked_stone_count)]) - max_relative_scores[picked_stone_count - 1] for picked_stone_count in [1, 2, 3])
            max_relative_scores[2], max_relative_scores[1], max_relative_scores[0] = max_relative_scores[1], max_relative_scores[0], curr_max_relative_score

        if max_relative_scores[0] == 0:
            return 'Tie'
        return 'Alice' if max_relative_scores[0] > 0 else 'Bob'
