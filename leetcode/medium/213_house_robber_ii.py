# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        max_money_rob_from_0 = [0] * len(nums)
        max_money_rob_from_1 = [0] * len(nums)
        max_money_rob_from_0[0] = nums[0]
        max_money_rob_from_1[1] = nums[1]
        for index in range(2, len(nums)):
            if index == 2:
                max_money_rob_from_0[2] = nums[2] + nums[0]
                max_money_rob_from_1[2] = nums[1]
            elif index == len(nums) - 1:
                max_money_rob_from_0[index] = max(
                    max_money_rob_from_0[index - 1],
                    nums[index] + max(max_money_rob_from_0[index - 2], max_money_rob_from_0[index - 3]) - nums[0],
                )
                max_money_rob_from_1[index] = nums[index] + max(max_money_rob_from_1[index - 2], max_money_rob_from_1[index - 3])
            else:
                max_money_rob_from_0[index] = nums[index] + max(max_money_rob_from_0[index - 2], max_money_rob_from_0[index - 3])
                max_money_rob_from_1[index] = nums[index] + max(max_money_rob_from_1[index - 2], max_money_rob_from_1[index - 3])
        
        return max(max(max_money_rob_from_0), max(max_money_rob_from_1))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82982325
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        self.nums = nums
        return max(self.rob_in_range(0, len(nums) - 2), self.rob_in_range(1, len(nums) - 1))

    def rob_in_range(self, start_index, end_index):
        max_money, prev_money_1, prev_money_2 = 0, 0, 0
        for index in range(start_index, end_index + 1):
            max_money = max(prev_money_1, self.nums[index] + prev_money_2)
            prev_money_2 = prev_money_1
            prev_money_1 = max_money

        return max_money
