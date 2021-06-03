# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^5)
# Space Complexity: O(n^4)
# -----------------------------------------
from collections import Counter
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def scrambled(s1, s2):
            if len(s1) != len(s2) or Counter(s1) != Counter(s2):
                return False
            if s1 == s2:
                return True

            for index in range(1, len(s1)):
                s1_sub_1, s1_sub_2 = s1[:index], s1[index:]
                if scrambled(s1_sub_1, s2[:index]) and scrambled(s1_sub_2, s2[index:]) or scrambled(s1_sub_2, s2[:-index]) and scrambled(s1_sub_1, s2[-index:]):
                    return True
            return False

        return scrambled(s1, s2)

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^4)
# Space Complexity: O(n^3)
# -----------------------------------------
# Ref: https://blog.csdn.net/linhuanmars/article/details/24506703
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False

        # dp[i][j][len] := self.isScramble(s1[i:(i + len)], s2[j:(j + len)])
        dp = [[[False] * (len(s1) + 1) for _ in range(len(s2))] for _ in range(len(s1))]
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i][j][1] = s1[i] == s2[j]

        for s_len in range(2, len(s1) + 1):
            for i in range(len(s1) - s_len + 1):
                for j in range(len(s2) - s_len + 1):
                    for k in range(1, s_len):
                        # self.isScramble(s1[i:(i + k)], s2[j:(j + k)]) and self.isScramble(s1[(i + k):(i + s_len)], s2[(j + k):(j + s_len)])
                        # or
                        # self.isScramble(s1[i:(i + k)], s2[(j + s_len - k):(j + s_len)]) and self.isScramble(s1[(i + k):(i + s_len)], s2[j:(j + s_len - k)])
                        # e.g. s1 == "great", s2 == "rgeat"
                        #      s_len == 5, k == 2
                        #      => self.isScramble("gr", "rg") and self.isScramble("eat", "eat") or self.isScramble("gr", "at") and self.isScramble("eat", "rge")
                        dp[i][j][s_len] |= dp[i][j][k] and dp[i + k][j + k][s_len - k] or dp[i][j + s_len - k][k] and dp[i + k][j][s_len - k]
        return dp[0][0][len(s1)]
