# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict
import bisect

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_indexes_map = defaultdict(list)
        for index, char in enumerate(s):
            char_indexes_map[char].append(index)

        curr_chars_set = set()
        max_len = 0
        for index, char in enumerate(s):
            if char in curr_chars_set:
                max_len = max(max_len, len(curr_chars_set))
                prev_index = char_indexes_map[char][bisect.bisect_left(char_indexes_map[char], index) - 1]
                curr_chars_set = set(s[(prev_index + 1):(index + 1)])
            else:
                curr_chars_set.add(char)

        return max(max_len, len(curr_chars_set))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82022530
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = {}
        max_len = 0
        while right < len(s):
            if s[right] in chars:
                max_len = max(max_len, right - left)
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            right += 1

        return max(max_len, right - left)
