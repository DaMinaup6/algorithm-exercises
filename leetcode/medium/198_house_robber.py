# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# dp[i] := the max money we can rob from first house to ith house
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        max_rob = nums[0]
        for index in range(1, len(nums)):
            if index == 1:
                dp[1] = nums[1]
            else:
                cur_num = nums[index]
                max_val = max(cur_num + dp[index - 2], cur_num + dp[index - 3]) if index > 2 else cur_num + dp[0]
                dp[index] = max_val
            max_rob = max(max_rob, dp[index])

        return max_rob
