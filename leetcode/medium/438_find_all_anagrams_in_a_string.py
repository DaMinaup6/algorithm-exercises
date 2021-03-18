# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n - m)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(p), n := len(s)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) == 0 or len(p) == 0 or len(s) < len(p):
            return []

        target_char_count_arr  = self.ganerate_char_count_arr(p)
        current_char_count_arr = self.ganerate_char_count_arr(s[0:len(p)])

        output = []
        if current_char_count_arr == target_char_count_arr:
            output.append(0)

        for index in range(1, len(s) - len(p) + 1):
            old_index = index - 1
            new_index = index + len(p) - 1
            current_char_count_arr[ord(s[old_index]) - 97] -= 1
            current_char_count_arr[ord(s[new_index]) - 97] += 1
            if current_char_count_arr == target_char_count_arr:
                output.append(index)

        return output

    def ganerate_char_count_arr(self, string):
        char_count_arr = [0] * 26
        for char in string:
            char_count_arr[ord(char) - 97] += 1

        return char_count_arr
