# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
import math

class Solution:
    def minElements(self, nums, limit, goal):
        current_sum  = sum(nums)
        current_diff = abs(goal - current_sum)
        
        return math.ceil(current_diff / limit)
