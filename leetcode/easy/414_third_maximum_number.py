# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = [-float('inf')] * 3
        for num in nums:
            if num > max_nums[0]:
                max_nums[0], max_nums[1], max_nums[2] = num, max_nums[0], max_nums[1]
            elif num > max_nums[1] and num != max_nums[0]:
                max_nums[1], max_nums[2] = num, max_nums[1]
            elif num > max_nums[2] and num not in max_nums[0:2]:
                max_nums[2] = num

        return max_nums[2] if max_nums[2] != -float('inf') else max_nums[0]
