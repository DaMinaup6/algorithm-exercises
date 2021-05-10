# -----------------------------------------
# My Solution
#
# Time  Complexity: O(2n)
# Space Complexity: O(2n)
# -----------------------------------------
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        right_greater = [-1] * (2 * len(nums))
        doubled_nums  = nums + nums
        stack = []
        for index in range(len(doubled_nums) - 1, -1, -1):
            num = doubled_nums[index]
            while len(stack) > 0 and stack[-1] <= num:
                stack.pop()
            if len(stack) > 0:
                right_greater[index] = stack[-1]
            stack.append(num)

        return right_greater[:len(nums)]
