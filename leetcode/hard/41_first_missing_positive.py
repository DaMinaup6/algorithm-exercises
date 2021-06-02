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
        # e.g. nums == [7, 3, 1, 9] => our target is to get modified array like [1, x, 3, y] where x and y are 7 or 9, doesn't matter which one is on which position
        #      when idx == 1, we want to swap 3 with the element nums[2] since 3 needed to be put at index 2, we we get [7, 1, 3, 9]
        #      and 1 needed to be put at index 0, so that's why we need a while loop here
        #      need to notice that if nums == [7, 3, 2, 9], after 3 swap with 2, need to break the while loop since 2 is already on its correct position
        #      if not break the while loop then it won't stop
        for idx in range(0, len(nums)):
            while 0 < nums[idx] <= len(nums) and nums[idx] != nums[nums[idx] - 1]:
                idx_2 = nums[idx] - 1
                nums[idx], nums[idx_2] = nums[idx_2], nums[idx]

        for idx in range(0, len(nums)):
            if nums[idx] != idx + 1:
                return idx + 1

        return len(nums) + 1
