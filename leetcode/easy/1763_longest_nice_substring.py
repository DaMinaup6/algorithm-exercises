# -----------------------------------------
# My Solution: Sliding Window
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def valid_nice_string(substring):
            char_set = set(substring)
            for char in substring:
                if char.lower() not in char_set or char.upper() not in char_set:
                    return False
            return True

        for window_size in range(len(s), 1, -1):
            for window_start in range(len(s) - window_size + 1):
                substring = s[window_start:(window_start + window_size)]
                if valid_nice_string(substring):
                    return substring
        return ""

# -----------------------------------------
# Model Solution: Divide and Conquer
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/longest-nice-substring/discuss/1074990/Python-3-recursion-100
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def find_nice_string(string):
            if len(string) <= 1:
                return ""

            char_set = set(string)
            pivot = -1
            for index, char in enumerate(string):
                if char.upper() not in char_set or char.lower() not in char_set:
                    pivot = index
                    break

            if pivot == -1:
                return string
            return max(find_nice_string(string[:pivot]), find_nice_string(string[(pivot + 1):]), key=len)

        return find_nice_string(s)
