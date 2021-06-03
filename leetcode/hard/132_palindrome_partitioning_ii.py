# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/qq_37821701/article/details/108619589
class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0

        # dp[i] := minimum cuts needed for s[:i]
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = -1
        for i in range(1, len(s) + 1):
            for j in range(1, i + 1):
                if s[(j - 1):i] == s[(j - 1):i][::-1]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]

# -----------------------------------------
# Model Solution
#
# Time Complexity: O(n^2)
# -----------------------------------------
# Ref:
# a) https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-132-palindrome-partitioning-ii/
# b) https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42205/56-ms-python-with-explanation

# -----> Version 1: Space Complexity: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0

        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                is_palindrome[j][i] = (s[i] == s[j]) and ((i - j < 2) or is_palindrome[j + 1][i - 1])

        # dp[i] := minimum cuts needed for s[:i]
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = -1
        for i in range(1, len(s) + 1):
            for j in range(1, i + 1):
                if is_palindrome[j - 1][i - 1]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def minCut(self, s: str) -> int:
        # dp[i] := minimum cuts needed for s[:i]
        # for string with length i, it needs i - 1 cuts at most
        # e.g. s == "abcde", then we need 4 cuts to get ["a", "b", "c", "d", "e"]
        # set dp[0] == -1 for strings are already palindrome
        # e.g. s == "aba", then with dp[0] == -1 we get dp[-1] = 0
        dp = [cut for cut in range(-1, len(s))]
        for index in range(len(s)):
            # odd length palindrome
            left_pointer, right_pointer = index, index
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                dp[right_pointer + 1] = min(dp[right_pointer + 1], dp[left_pointer] + 1)
                left_pointer  -= 1
                right_pointer += 1
            # even length palindrome
            left_pointer, right_pointer = index, index + 1
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                dp[right_pointer + 1] = min(dp[right_pointer + 1], dp[left_pointer] + 1)
                left_pointer  -= 1
                right_pointer += 1

        return dp[-1]
