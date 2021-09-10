# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(nums)
#
# Ref: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total, n = 0, len(nums)

        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)
            total += sum(dp[i].values())

        # substract by C^n_2 since we need at least 3 elements in subsequence
        return total - (n - 1) * n // 2
