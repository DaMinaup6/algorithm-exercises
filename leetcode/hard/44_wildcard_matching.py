# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(mn)
# -----------------------------------------
# m := len(s), n := len(p)

# -----> Version 1: Space Complexity: O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # for sub_s_len == 0, the only pattern to match is single or multiple *
        for sub_p_len in range(1, len(p) + 1):
            dp[0][sub_p_len] = (p[sub_p_len - 1] == '*') and dp[0][sub_p_len - 1]

        for sub_s_len in range(1, len(s) + 1):
            for sub_p_len in range(1, len(p) + 1):
                curr_s_char = s[sub_s_len - 1]
                curr_p_char = p[sub_p_len - 1]
                if curr_s_char == curr_p_char or curr_p_char == '?':
                    dp[sub_s_len][sub_p_len] = dp[sub_s_len - 1][sub_p_len - 1]
                elif curr_p_char == '*':
                    dp[sub_s_len][sub_p_len] = dp[sub_s_len][sub_p_len - 1] or dp[sub_s_len - 1][sub_p_len]
        return dp[-1][-1]

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp_curr = [False] * (len(p) + 1)
        dp_curr[0] = True

        for sub_p_len in range(1, len(p) + 1):
            dp_curr[sub_p_len] = (p[sub_p_len - 1] == '*') and dp_curr[sub_p_len - 1]

        for sub_s_len in range(1, len(s) + 1):
            dp_next = [False] * (len(p) + 1)
            for sub_p_len in range(1, len(p) + 1):
                curr_s_char = s[sub_s_len - 1]
                curr_p_char = p[sub_p_len - 1]
                if curr_s_char == curr_p_char or curr_p_char == '?':
                    dp_next[sub_p_len] = dp_curr[sub_p_len - 1]
                elif curr_p_char == '*':
                    dp_next[sub_p_len] = dp_next[sub_p_len - 1] or dp_curr[sub_p_len]
            dp_curr = dp_next
        return dp_curr[-1]
