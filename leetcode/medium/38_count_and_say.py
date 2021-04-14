# -----------------------------------------
# My Solution
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^(n - 1))
# -----------------------------------------
# Note: the worst case is that any two adjacent digit in the sequence are not identical, then its next sequence would double the length
class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'
        for _ in range(2, n + 1):
            contiguous_digits_count = []
            curr_digit = output[0]
            curr_count = 1

            output += '*'
            for index in range(1, len(output)):
                digit = output[index]
                if digit == curr_digit:
                    curr_count += 1
                else:
                    contiguous_digits_count.append([curr_count, curr_digit])
                    curr_digit = digit
                    curr_count = 1
            
            output = ''
            for digit_count, digit in contiguous_digits_count:
                output += str(digit_count) + str(digit)

        return output

# -----------------------------------------
# Model Solution: Regular Expression
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^(n - 1))
# -----------------------------------------
# Ref: https://leetcode.com/problems/count-and-say/solution/
import re

class Solution:
    def countAndSay(self, n: int) -> str:
        curr_str = '1'
        pattern  = r'((.)\2*)'

        for _ in range(n - 1):
            next_str = ''
            for group_1, grouop_2 in re.findall(pattern, curr_str):
                # append the pair of <count, digit>
                next_str += str(len(group_1)) + grouop_2
            # prepare for the next iteration
            curr_str = next_str

        return curr_str
