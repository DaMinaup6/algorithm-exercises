# -----------------------------------------
# My Solution: Two Pointers
#
# Time  Complexity: O(m + n)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(s), n := len(t)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_non_empty_char_index(string, start_index):
            char_index = start_index

            # e.g. string == "bxo#j##tw"
            backspace_count = 0
            while char_index >= 0 and (string[char_index] == "#" or backspace_count > 0):
                backspace_count += 1 if string[char_index] == "#" else -1
                char_index -= 1
            return char_index

        s_pointer, t_pointer = len(s) - 1, len(t) - 1
        while s_pointer >= 0 or t_pointer >= 0:
            s_pointer = find_non_empty_char_index(s, s_pointer)
            t_pointer = find_non_empty_char_index(t, t_pointer)

            s_char = s[s_pointer] if s_pointer >= 0 else ""
            t_char = t[t_pointer] if t_pointer >= 0 else ""
            if s_char != t_char:
                return False
            s_pointer -= 1
            t_pointer -= 1

        return True
