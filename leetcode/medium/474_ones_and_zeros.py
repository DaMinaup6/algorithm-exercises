# -----------------------------------------
# My Solution
#
# Time  Complexity: O(s * (mn + max_str_len))
# Space Complexity: O(smn)
# -----------------------------------------
# s := len(strs), max_str_len := max(strs[i])
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[k][i][j] := max subset we can have for strs[:k] with at most i zeros and j ones
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for k in range(1, len(strs) + 1):
            digit_counter = Counter(strs[k - 1])
            zero_count = digit_counter['0']
            one_count  = digit_counter['1']
            for i in range(m + 1):
                for j in range(n + 1):
                    if i >= zero_count and j >= one_count:
                        dp[k][i][j] = max(dp[k - 1][i][j], dp[k - 1][i - zero_count][j - one_count] + 1)
                    else:
                        dp[k][i][j] = dp[k - 1][i][j]
        return dp[len(strs)][m][n]

# -----------------------------------------
# Space Complexity Enhanced Solution
#
# Time  Complexity: O(s * (mn + max_str_len))
# Space Complexity: O(mn)
# -----------------------------------------
# s := len(strs), max_str_len := max(strs[i])
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        curr_dp = [[0] * (n + 1) for _ in range(m + 1)]
        for k in range(1, len(strs) + 1):
            digit_counter = Counter(strs[k - 1])
            zero_count = digit_counter['0']
            one_count  = digit_counter['1']

            next_dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i >= zero_count and j >= one_count:
                        next_dp[i][j] = max(curr_dp[i][j], curr_dp[i - zero_count][j - one_count] + 1)
                    else:
                        next_dp[i][j] = curr_dp[i][j]
            curr_dp = next_dp
        return curr_dp[m][n]
