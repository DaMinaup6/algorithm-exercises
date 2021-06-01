# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(mn)
# Space Complexity: O(m)
# -----------------------------------------
# m := target, n := len(nums)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [0] * (target + 1)
        for possible_sum in range(1, target + 1):
            for num in nums:
                if num == possible_sum:
                    dp[possible_sum] += 1
                elif num < possible_sum:
                    dp[possible_sum] += dp[possible_sum - num]
        return dp[-1]
