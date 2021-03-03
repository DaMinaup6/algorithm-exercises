# -----------------------------------------
# My Solution
# -----------------------------------------
# class Solution:
#     def firstMissingPositive(self, nums):
#         if len(nums) == 0:
#             return 1
#
#         max_positive_num = 0
#         min_positive_num = float('inf')
#         for num in nums:
#             if num > 0:
#                 if num > max_positive_num:
#                     max_positive_num = num
#                 if num < min_positive_num:
#                     min_positive_num = num
#         if max_positive_num <= 0 or min_positive_num >= 2:
#             return 1
#         elif max_positive_num <= 2:
#             return max_positive_num + 1
#
#         num_set = set()
#         for num in nums:
#             if 1 < num < max_positive_num:
#                 num_set.add(num)
#         if len(num_set) == 0:
#             return 2
#         elif len(num_set) == max_positive_num - 2:
#             return max_positive_num + 1
#
#         range_set = set(range(2, len(num_set) + 3))
#         for num in num_set:
#             if num in range_set:
#                 range_set.remove(num)
#
#         return min(range_set)

# -----------------------------------------
# Model Solution
# -----------------------------------------
class Solution:
    def firstMissingPositive(self, nums):
        for idx in range(0, len(nums)):
            while 0 < nums[idx] <= len(nums) and nums[idx] != nums[nums[idx] - 1]:
                idx_2 = nums[idx] - 1
                nums[idx], nums[idx_2] = nums[idx_2], nums[idx]

        for idx in range(0, len(nums)):
            if nums[idx] != idx + 1:
                return idx + 1

        return len(nums) + 1
