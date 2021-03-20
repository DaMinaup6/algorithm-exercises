# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2 * 2^(2n))
# Space Complexity: O(2^(2n))
# -----------------------------------------
# Ref: https://leetcode.com/problems/maximize-score-after-n-operations/discuss/1118782/Python3-dp
from functools import lru_cache
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(nums, k_th_operation):
            if not nums:
                return 0 # boundary condition 

            ans = 0 
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    rest_nums = nums[:i] + nums[(i + 1):j] + nums[(j + 1):]
                    ans = max(ans, k_th_operation * gcd(nums[i], nums[j]) + helper(tuple(rest_nums), k_th_operation + 1))
            return ans
        
        return helper(tuple(nums), 1)
