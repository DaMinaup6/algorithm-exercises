# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(s - n))
# Space Complexity: O(1)
# -----------------------------------------
# s := maxSum
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left  = 1
        right = maxSum - n + 1
        while left <= right:
            middle = (left + right) // 2
            middle_val = self.value_at_index_sum(n, index, middle)

            if middle_val == maxSum:
                return middle
            elif middle_val > maxSum:
                right = middle - 1
            else:
                left = middle + 1

        return left - 1

    def value_at_index_sum(self, n: int, index: int, val: int) -> int:
        left_sum = 0
        if index > 0:
            if index + 1 >= val:
                left_sum = val * (val - 1) // 2 + (index + 1 - val)
            else:
                left_sum = (2 * val - index - 1) * index // 2
        right_sum = 0
        if index < n - 1:
            if n - index >= val:
                right_sum = val * (val - 1) // 2 + (n - index - val)
            else:
                right_sum = (2 * val + index - n) * (n - index - 1) // 2

        return val + left_sum + right_sum

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119794/Python-O(1)-Math-solution
import math

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n              # remove the contributions from all the 1 in each element.
                                 # We will add 1 back to the final height later
        if index < n // 2:       # make the index closer to the right boundary
            index = n - index - 1
        n_left = index           # number of element to the left of the index
        n_right = n - 1 - index  # number of element to the right of the index
        tri_left = (n_left * (n_left + 1)) // 2     # the triangle area for the left side if not hitting the boundary
        tri_right = (n_right * (n_right + 1)) // 2  # the triangle area for the right side if not hitting the boundary
        # case 1: perfect pyramid
        if maxSum <= (tri_right * 2 + n_right + 1):
            return int(math.sqrt(maxSum)) + 1
        # case 2: right side hits the boundary
        if maxSum <= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1):
            b = 3 + 2 * n_right
            return int((-b + math.sqrt(b * b - 8 * (tri_right + 1 - n_right * n_right - maxSum))) / 2) + 1 + 1
        # case 3: both sides hit boundaries
        maxSum -= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
        return n_left + 1 + 1 + (maxSum // n)
