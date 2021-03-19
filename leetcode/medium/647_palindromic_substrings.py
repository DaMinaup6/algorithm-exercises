# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(set([char for char in s])) == 1:
            return (len(s) + 1) * len(s) // 2

        result = len(s)
        for window_size in range(len(s), 1, -1):
            for index in range(len(s) - window_size + 1):
                if self.is_palindromic(s, index, index + window_size - 1):
                    result += 1

        return result

    def is_palindromic(self, s: str, start_index: int, end_index: int) -> bool:
        for index in range((end_index - start_index + 1) // 2):
            if s[start_index + index] != s[end_index - index]:
                return False

        return True

# -----------------------------------------
# Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79433960
class Solution(object):
    def countSubstrings(self, s):
        # dp[i][j] := s[i:(j + 1)] is palindromic or not
        dp  = [[False] * len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            dp[i][i] = True
            ans += 1

            for j in range(i):
                # if s[i:j] is palindromic
                # a) s[i] == s[j]
                # b) s[(i + 1):j] is palindromic (if j - i >= 2)
                if i - j < 2:
                    dp[j][i] = s[j] == s[i]
                else:
                    dp[j][i] = s[j] == s[i] and dp[j + 1][i - 1]

                if dp[j][i]:
                    ans += 1

        return ans

# -----------------------------------------
# Expand Around Possible Centers
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79433960
class Solution(object):
    def countSubstrings(self, s):
        ans = 0
        for index in range(len(s)):
            ans += 1
            # length of palindromic substrings is odd
            left  = index - 1
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans   += 1
                left  -= 1
                right += 1
            # length of palindromic substrings is even
            left  = index
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans   += 1
                left  -= 1
                right += 1

        return ans
