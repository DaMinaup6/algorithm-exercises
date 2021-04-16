# -----------------------------------------
# My Solution
#
# Time  Complexity: O(26 * n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(s)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_repeating_characters = k
        for curr_target in set(s):
            left_pointer, right_pointer = 0, k
            remains_jump = s[0:k].count(curr_target)
            while right_pointer < len(s):
                if s[right_pointer] == curr_target:
                    right_pointer += 1
                elif remains_jump > 0:
                    remains_jump  -= 1
                    right_pointer += 1
                else:
                    longest_repeating_characters = max(longest_repeating_characters, right_pointer - left_pointer)
                    while left_pointer < right_pointer and s[left_pointer] == curr_target:
                        left_pointer += 1
                    left_pointer  += 1
                    right_pointer += 1
            longest_repeating_characters = max(longest_repeating_characters, right_pointer - left_pointer)

        return longest_repeating_characters

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(s)
# Ref:
# a) https://www.youtube.com/watch?v=00FmUN1pkGE
# b) https://www.youtube.com/watch?v=SLAKjysDODM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = [0] * 26

        window_start = 0
        curr_char_count_max = 0
        longest_repeating_characters = 0

        for window_end in range(len(s)):
            char_index = ord(s[window_end]) - ord('A')
            char_counts[char_index] += 1
            curr_char_count_max = max(curr_char_count_max, char_counts[char_index])

            if (window_end - window_start + 1) - curr_char_count_max > k:
                char_index = ord(s[window_start]) - ord('A')
                char_counts[char_index] -= 1
                window_start += 1

            longest_repeating_characters = max(longest_repeating_characters, window_end - window_start + 1)

        return longest_repeating_characters
