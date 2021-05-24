# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Note: the space complexity is O(26) since we can have at most 26 characters in counter
from collections import Counter

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        a_char_counter = Counter(a)
        b_char_counter = Counter(b)
        if a_char_counter != b_char_counter:
            return False

        char_diff = 0
        for index in range(len(a)):
            if a[index] != b[index]:
                char_diff += 1
            if char_diff > 2:
                return False
        if char_diff == 0:
            return any(a_char_counter[char] >= 2 for char in a_char_counter)
        return char_diff == 2

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/buddy-strings/solution/
class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        diff_pairs = []
        for index in range(len(a)):
            if a[index] != b[index]:
                if len(diff_pairs) == 2:
                    return False
                diff_pairs.append([a[index], b[index]])

        if len(diff_pairs) == 0:
            seen_chars = set()
            for char in a:
                if char in seen_chars:
                    return True
                seen_chars.add(char)
            return False

        return len(diff_pairs) == 2 and diff_pairs[0] == diff_pairs[1][::-1]
