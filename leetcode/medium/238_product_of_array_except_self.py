# -----------------------------------------
# Model Solution
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products  = [1] * len(nums)
        right_products = [1] * len(nums)

        for index in range(1, len(nums)):
            left_products[index] = left_products[index - 1] * nums[index - 1]
        for index in range(len(nums) - 2, -1, -1):
            right_products[index] = right_products[index + 1] * nums[index + 1]

        return [left_products[index] * right_products[index] for index in range(len(nums))]

# -----> Version 2: Space Complexity: O(1)
# Note: output does not count as extra space for space complexity analysis here
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        curr_left_product, curr_right_product = 1, 1
        left_index, right_index = 1, len(nums) - 2
        for _ in range(len(nums) - 1):
            curr_left_product  = curr_left_product  * nums[left_index  - 1]
            curr_right_product = curr_right_product * nums[right_index + 1]
            output[left_index]  *= curr_left_product
            output[right_index] *= curr_right_product
            left_index  += 1
            right_index -= 1
        return output
