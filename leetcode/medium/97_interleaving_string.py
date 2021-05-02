# -----------------------------------------
# My Solution: Recursion + Memoization
#
# Time  Complexity: O(mn + k + m + n)
# Space Complexity: O(mn + k + m + n)
# -----------------------------------------
# m := len(s1), n := len(s2), k := len(s3)
from collections import Counter
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) or Counter(s1) + Counter(s2) != Counter(s3):
            return False

        @lru_cache(None)
        def dfs(s1_index, s2_index):
            if s1_index + s2_index == len(s3):
                return True

            s1_char = s1[s1_index] if s1_index < len(s1) else ''
            s2_char = s2[s2_index] if s2_index < len(s2) else ''
            s3_char = s3[s1_index + s2_index]
            if s3_char not in [s1_char, s2_char]:
                return False
            if s3_char == s1_char and s3_char != s2_char:
                return dfs(s1_index + 1, s2_index)
            if s3_char != s1_char and s3_char == s2_char:
                return dfs(s1_index, s2_index + 1)
            return dfs(s1_index + 1, s2_index) or dfs(s1_index, s2_index + 1)

        return dfs(0, 0)

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(mn)
# -----------------------------------------
# m := len(s1), n := len(s2), k := len(s3)

# -----> Version 1: Space Complexity: O(mn)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for s1_index in range(len(s1), -1, -1):
            for s2_index in range(len(s2), -1, -1):
                if s1_index + s2_index == len(s3):
                    dp[s1_index][s2_index] = True
                    continue

                s1_char = s1[s1_index] if s1_index < len(s1) else ''
                s2_char = s2[s2_index] if s2_index < len(s2) else ''
                s3_char = s3[s1_index + s2_index]
                if s3_char in [s1_char, s2_char]:
                    if s1_char != s2_char:
                        dp[s1_index][s2_index] = dp[s1_index + 1][s2_index] if s3_char == s1_char else dp[s1_index][s2_index + 1]
                    else:
                        dp[s1_index][s2_index] = dp[s1_index + 1][s2_index] or dp[s1_index][s2_index + 1]

        return dp[0][0]

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        curr_dp = [False] * (len(s2) + 1)
        for s1_index in range(len(s1), -1, -1):
            next_dp = [False] * (len(s2) + 1)
            for s2_index in range(len(s2), -1, -1):
                if s1_index + s2_index == len(s3):
                    next_dp[s2_index] = True
                    continue

                s1_char = s1[s1_index] if s1_index < len(s1) else ''
                s2_char = s2[s2_index] if s2_index < len(s2) else ''
                s3_char = s3[s1_index + s2_index]
                if s3_char in [s1_char, s2_char]:
                    if s1_char != s2_char:
                        next_dp[s2_index] = curr_dp[s2_index] if s3_char == s1_char else next_dp[s2_index + 1]
                    else:
                        next_dp[s2_index] = curr_dp[s2_index] or next_dp[s2_index + 1]
            curr_dp = next_dp

        return curr_dp[0]
