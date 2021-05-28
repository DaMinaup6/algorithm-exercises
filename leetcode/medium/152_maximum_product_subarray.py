# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from functools import reduce

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        non_zero_nums = []
        max_val = -float('inf')

        for num in nums:
            if num == 0:
                max_val = max(max_val, 0, self.max_product(non_zero_nums))
                non_zero_nums = []
            else:
                non_zero_nums.append(num)

        return max(max_val, self.max_product(non_zero_nums))

    def max_product(self, non_zero_nums):
        if len(non_zero_nums) == 0:
            return -float('inf')

        neg_indices = []
        for index in range(len(non_zero_nums)):
            if non_zero_nums[index] < 0:
                neg_indices.append(index)

        if len(neg_indices) % 2 == 0:
            return reduce(lambda a, b: a * b, non_zero_nums)
        elif len(neg_indices) == 1:
            key_values = [non_zero_nums[neg_indices[0]]]
            if neg_indices[0] > 0:
                key_values.append(reduce(lambda a, b: a * b, non_zero_nums[:neg_indices[0]]))
            if neg_indices[0] < len(non_zero_nums) - 1:
                key_values.append(reduce(lambda a, b: a * b, non_zero_nums[(neg_indices[0] + 1):]))

            return max(key_values)
        else:
            first_neg_idx, last_neg_idx = neg_indices[0], neg_indices[-1]
            prod_before_first_neg  = reduce(lambda a, b: a * b, non_zero_nums[:first_neg_idx]) if first_neg_idx > 0 else 1
            prod_in_first_last_neg = reduce(lambda a, b: a * b, non_zero_nums[(first_neg_idx + 1):last_neg_idx])
            prod_after_last_neg    = reduce(lambda a, b: a * b, non_zero_nums[(last_neg_idx + 1):]) if last_neg_idx < len(non_zero_nums) - 1 else 1

            return max(prod_before_first_neg * non_zero_nums[first_neg_idx] * prod_in_first_last_neg, prod_in_first_last_neg * non_zero_nums[last_neg_idx] * prod_after_last_neg)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max_val = curr_min_val = max_val = nums[0]
        for index in range(1, len(nums)):
            prev_max_val, prev_min_val = curr_max_val, curr_min_val
            curr_max_val = max(prev_max_val * nums[index], prev_min_val * nums[index], nums[index])
            curr_min_val = min(prev_max_val * nums[index], prev_min_val * nums[index], nums[index])
            max_val = max(max_val, curr_max_val)
        return max_val
