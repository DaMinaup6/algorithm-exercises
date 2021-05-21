# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        char_num_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        integer = 0
        pointer = 0
        while pointer < len(s):
            # this condition only statisfied when roman is IV or IX or XL or ...
            if pointer < len(s) - 1 and char_num_mapping[s[pointer]] < char_num_mapping[s[pointer + 1]]:
                integer += char_num_mapping[s[pointer + 1]] - char_num_mapping[s[pointer]]
                pointer += 2
            else:
                integer += char_num_mapping[s[pointer]]
                pointer += 1
        return integer
