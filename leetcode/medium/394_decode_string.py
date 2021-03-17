# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def decodeString(self, s: str) -> str:
        encoded_list = []

        output = ''
        for char in s:
            if char.isdigit():
                # e.g. "100[leetcode]", "3[2[a]]"
                if len(encoded_list) > 0 and encoded_list[-1][0][-1] != '[':
                    encoded_list[-1][0] += char
                else:
                    encoded_list.append([char, ''])
            elif char == '[':
                # add "[" to end appending number since there can be "100[" or "1["
                encoded_list[-1][0] += '['
            elif char == ']':
                encoded_info = encoded_list.pop()
                encoded_str  = encoded_info[1] * int(encoded_info[0][:-1])

                # e.g. "3[a2[c]]"
                if len(encoded_list) > 0:
                    encoded_list[-1][1] += encoded_str
                else:
                    output += encoded_str
            elif len(encoded_list) > 0:
                encoded_list[-1][1] += char
            else:
                output += char

        return output
