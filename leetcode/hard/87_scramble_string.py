# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^5)
# Space Complexity: O(n^4)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.scrambled(s1, s2)

    @lru_cache(None)
    def scrambled(self, s1, s2):
        if s1 == s2:
            return True

        s1_char_count = [0] * 26
        s2_char_count = [0] * 26
        for index in range(len(s1)):
            s1_char_idx = ord(s1[index]) - ord('a')
            s2_char_idx = ord(s2[index]) - ord('a')
            s1_char_count[s1_char_idx] += 1
            s2_char_count[s2_char_idx] += 1
        if s1_char_count != s2_char_count:
            return False
        if len(s1) <= 3:
            return True

        for index in range(1, len(s1)):
            s1_sub_1 = s1[:index]
            s1_sub_2 = s1[index:]
            if self.scrambled(s1_sub_1, s2[:index]) and self.scrambled(s1_sub_2, s2[index:]) or self.scrambled(s1_sub_2, s2[:-index]) and self.scrambled(s1_sub_1, s2[-index:]):
                return True
        return False

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^4)
# Space Complexity: O(n^3)
# -----------------------------------------
# Ref: https://blog.csdn.net/linhuanmars/article/details/24506703
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_char_count = [0] * 26
        s2_char_count = [0] * 26
        for index in range(len(s1)):
            s1_char_idx = ord(s1[index]) - ord('a')
            s2_char_idx = ord(s2[index]) - ord('a')
            s1_char_count[s1_char_idx] += 1
            s2_char_count[s2_char_idx] += 1
        if s1_char_count != s2_char_count:
            return False
        if len(s1) <= 3:
            return True

        # dp[i][j][len] := self.isScramble(s1[i:(i + len)], s2[j:(j + len)])
        dp = [[[False] * (len(s1) + 1) for _ in range(len(s1))] for _ in range(len(s1))]
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i][j][1] = s1[i] == s2[j]

        for s_len in range(2, len(s1) + 1):
            for i in range(len(s1) - s_len + 1):
                for j in range(len(s2) - s_len + 1):
                    for k in range(1, s_len):
                        dp[i][j][s_len] |= dp[i][j][k] and dp[i + k][j + k][s_len - k] or dp[i][j + s_len - k][k] and dp[i + k][j][s_len - k]
        return dp[0][0][len(s1)]
