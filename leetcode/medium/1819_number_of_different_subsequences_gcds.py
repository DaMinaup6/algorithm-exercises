# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n + mlog(m))
# Space Complexity: O(n)
# -----------------------------------------
# m := max(nums), n := len(nums)
# Ref: https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1141547/Python-Test-every-GCD-(proof)-O(M-log-M)
from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        max_num = max(nums)

        ans = 0
        for num in range(1, max_num + 1):
            divisor = 0
            for num_multiplier in range(num, max_num + 1, num):
                if num_multiplier in nums:
                    divisor = gcd(divisor, num_multiplier)
                if divisor == num:
                    break

            if divisor == num:
                ans += 1
                
        return ans
