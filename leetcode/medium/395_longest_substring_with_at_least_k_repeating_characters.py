# -----------------------------------------
# Model Solution: Divide and Conquer
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(s)
# Ref:
# a) https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
# b) https://blog.csdn.net/fuxuemingzhu/article/details/82889933
from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        char_freq_count = defaultdict(int)
        for index, char in enumerate(s):
            char_freq_count[char] += 1
        if all(char_freq_count[char] < k for char in char_freq_count):
            return 0

        for index, char in enumerate(s):
            if char_freq_count[char] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))

        return len(s)

# -----------------------------------------
# Model Solution: Sliding Window
#
# Time  Complexity: O(26n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(s)
# Ref:
# a) https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
# b) https://maxming0.github.io/2020/11/26/Longest-Substring-with-At-Least-K-Repeating-Characters/
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        longest_substring_length = 0
        for max_unique_chars in range(1, len(set(s)) + 1):
            char_count = [0] * 26
            left_pointer = right_pointer = k_repeated_chars_count = unique_chars = 0
            while right_pointer < len(s):
                char_index = ord(s[right_pointer]) - ord('a')
                char_count[char_index] += 1
                if char_count[char_index] == 1:
                    unique_chars += 1
                if char_count[char_index] == k:
                    k_repeated_chars_count += 1
                right_pointer += 1
                
                while left_pointer < right_pointer and unique_chars > max_unique_chars:
                    char_index = ord(s[left_pointer]) - ord('a')
                    if char_count[char_index] == k:
                        k_repeated_chars_count -= 1
                    if char_count[char_index] == 1:
                        unique_chars -= 1
                    char_count[char_index] -= 1
                    left_pointer += 1
                if unique_chars == k_repeated_chars_count == max_unique_chars:
                    longest_substring_length = max(longest_substring_length, right_pointer - left_pointer)

        return longest_substring_length
