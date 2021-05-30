# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
# b) https://blog.csdn.net/Orientliu96/article/details/104117187

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        dp = [0] * len(nums)
        total_sum = 0
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                dp[index] = dp[index - 1] + 1
                total_sum += dp[index]
        return total_sum

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        # e.g. if now we have nums == [1, 2, 3, 4, 5], then there are 6 arithmetic subarrays, which are
        # [1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4], [2, 3, 4, 5] and [1, 2, 3, 4, 5]
        # this number equals 1 + 2 + 3 == 6
        # so starts from index 2, we found [1, 2, 3] is arithmetic subarray, now consecutive == 1
        # to index 3, we found [2, 3, 4] is arithmetic subarray, now consecutive == 2
        # to index 4, we found [3, 4, 5] is arithmetic subarray, now consecutive == 3
        # just add consecutive during for loop then we get the final answer
        consecutive = 0
        total_count = 0
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                consecutive += 1
                total_count += consecutive
            else:
                consecutive = 0
        return total_count
