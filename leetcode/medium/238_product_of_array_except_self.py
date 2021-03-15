# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products  = [1] * len(nums)
        right_products = [1] * len(nums)

        for index in range(1, len(nums)):
            left_products[index] = left_products[index - 1] * nums[index - 1]
        for index in range(len(nums) - 2, -1, -1):
            right_products[index] = right_products[index + 1] * nums[index + 1]

        return [left_products[index] * right_products[index] for index in range(len(nums))]
