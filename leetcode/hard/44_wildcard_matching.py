# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(s), n := len(p)
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

        return dp[len(s)][len(p)]

# -----------------------------------------
# My Solution: Space Compression
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(s), n := len(p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp_prev = [False] * (len(p) + 1)
        dp_curr = [False] * (len(p) + 1)
        dp_prev[0] = True

        for sub_p_len in range(1, len(p) + 1):
            dp_prev[sub_p_len] = (p[sub_p_len - 1] == '*') and dp_prev[sub_p_len - 1]

        for sub_s_len in range(1, len(s) + 1):
            for sub_p_len in range(1, len(p) + 1):
                curr_s_char = s[sub_s_len - 1]
                curr_p_char = p[sub_p_len - 1]
                if curr_s_char == curr_p_char or curr_p_char == '?':
                    dp_curr[sub_p_len] = dp_prev[sub_p_len - 1]
                elif curr_p_char == '*':
                    dp_curr[sub_p_len] = dp_curr[sub_p_len - 1] or dp_prev[sub_p_len]

            dp_prev = dp_curr
            dp_curr = [False] * (len(p) + 1)

        return dp_prev[len(p)]
