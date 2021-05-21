# -----------------------------------------
# My Solution
#
# Time  Complexity: O(ns)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(strs), s := min(string for string in strs)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        curr_pointer = 0
        while curr_pointer < len(strs[0]):
            curr_char = strs[0][curr_pointer]
            for index in range(1, len(strs)):
                if curr_pointer >= len(strs[index]) or strs[index][curr_pointer] != curr_char:
                    return strs[0][:curr_pointer]
            curr_pointer += 1
        return strs[0][:curr_pointer]
