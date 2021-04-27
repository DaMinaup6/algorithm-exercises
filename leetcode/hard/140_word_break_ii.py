# -----------------------------------------
# Model Solution: Recursion
#
# Time  Complexity: O(n * 2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
# n := len(s)
# Ref: https://leetcode.com/problems/word-break-ii/discuss/1178751/Python-Easy-to-understand-simple-dfs-accepted-solution(beats-83)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        combinations = []

        def dfs(curr_s, curr_combination):
            if len(curr_s) == 0:
                return
            if curr_s in word_set:
                combinations.append(curr_combination + curr_s)

            for index in range(1, len(curr_s)):
                sub_s = curr_s[:index]
                if sub_s in word_set:
                    dfs(curr_s[index:], curr_combination + sub_s + ' ')

        dfs(s, '')
        return combinations
