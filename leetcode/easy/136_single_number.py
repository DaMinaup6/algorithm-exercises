# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        return reduce(lambda a, b: a ^ b, nums)
