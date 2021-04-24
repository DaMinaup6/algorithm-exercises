# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n!)
# Space Complexity: O(n)
# -----------------------------------------
# Note: This solution causes TLE
from collections import Counter, defaultdict

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        s_chars_count, t_chars_count = Counter(s), Counter(t)
        for char in t_chars_count:
            if s_chars_count[char] < t_chars_count[char]:
                return 0

        s_char_indexes_dict = defaultdict(list)
        for index, char in enumerate(s):
            s_char_indexes_dict[char].append(index)

        total_count = 0
        def dfs(t_index, prev_index):
            nonlocal total_count
            
            if t_index == len(t):
                total_count += 1
            else:
                for possible_index in s_char_indexes_dict[t[t_index]]:
                    if possible_index > prev_index:
                        dfs(t_index + 1, possible_index)

        dfs(0, -1)
        return total_count

# -----------------------------------------
# My Solution
#
# Time Complexity: O(n^2)
# -----------------------------------------
# Ref:
# a) https://www.youtube.com/watch?v=mPqqXh8XvWY
# b) https://blog.csdn.net/aliceyangxi1987/article/details/51979042

# -----> Version 1: Space Complexity: O(n^2)
from collections import Counter

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        s_chars_count, t_chars_count = Counter(s), Counter(t)
        for char in t_chars_count:
            if s_chars_count[char] < t_chars_count[char]:
                return 0

        # dp[i][j] := number of subsequences of s[:j] equals t[:i]
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for index in range(len(s) + 1):
            dp[0][index] = 1

        for t_index in range(1, len(t) + 1):
            for s_index in range(1, len(s) + 1):
                if t[t_index - 1] == s[s_index - 1]:
                    # since t[t_index - 1] == s[s_index - 1]
                    # 1) for subsequences ends at s[s_index - 1], the number would be dp[t_index - 1][s_index - 1]
                    # 2) for subsequences not ends at s[s_index - 1], the number would be dp[t_index][s_index - 1]
                    dp[t_index][s_index] = dp[t_index - 1][s_index - 1] + dp[t_index][s_index - 1]
                else:
                    dp[t_index][s_index] = dp[t_index][s_index - 1]
        return dp[len(t)][len(s)]

# -----> Version 2: Space Complexity: O(n)
from collections import Counter

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        s_chars_count, t_chars_count = Counter(s), Counter(t)
        for char in t_chars_count:
            if s_chars_count[char] < t_chars_count[char]:
                return 0

        prev_dp = [1] * (len(s) + 1)
        for t_index in range(1, len(t) + 1):
            curr_dp = [0] * (len(s) + 1)
            for s_index in range(1, len(s) + 1):
                if t[t_index - 1] == s[s_index - 1]:
                    curr_dp[s_index] = prev_dp[s_index - 1] + curr_dp[s_index - 1]
                else:
                    curr_dp[s_index] = curr_dp[s_index - 1]
            prev_dp = curr_dp

        return curr_dp[len(s)]
