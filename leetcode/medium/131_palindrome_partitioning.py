# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n * 2^n)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(s)
from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]
        palindrome_start_end_map = defaultdict(list) # { start_index: [end_index_1, end_index_2, ...] }

        for i in range(len(s)):
            for j in range(i + 1):
                dp[j][i] = (s[i] == s[j]) and ((i - j < 2) or dp[j + 1][i - 1])
                if dp[j][i]:
                    palindrome_start_end_map[j].append(i)

        result = []
        def dfs(curr_partition, start_index):
            if start_index == len(s):
                result.append(curr_partition)
                return
            for end_index in palindrome_start_end_map[start_index]:
                dfs(curr_partition + [s[start_index:(end_index + 1)]], end_index + 1)
        dfs([], 0)

        return result
