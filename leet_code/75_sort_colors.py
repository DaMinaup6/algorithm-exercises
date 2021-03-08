# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# def move_zero_before_one(nums, positions):
#     one_indexes_equal = positions[1] == positions[2]
#
#     nums[positions[0]], nums[positions[1]] = nums[positions[1]], nums[positions[0]]
#     if one_indexes_equal:
#         positions[0], positions[1], positions[2] = positions[1], positions[0], positions[0]
#     else:
#         positions[0], positions[1], positions[2] = positions[1], positions[1] + 1, positions[0]
#
# def move_zero_before_two(nums, positions):
#     two_indexes_equal = positions[3] == positions[4]
#
#     nums[positions[0]], nums[positions[3]] = nums[positions[3]], nums[positions[0]]
#     if two_indexes_equal:
#         positions[0], positions[3], positions[4] = positions[3], positions[0], positions[0]
#     else:
#         positions[0], positions[3], positions[4] = positions[3], positions[3] + 1, positions[0]
#
# def move_one_before_two(nums, positions):
#     one_indexes_equal = positions[1] == positions[2]
#     two_indexes_equal = positions[3] == positions[4]
#
#     nums[positions[2]], nums[positions[3]] = nums[positions[3]], nums[positions[2]]
#     if one_indexes_equal:
#         if two_indexes_equal:
#             positions[1], positions[2], positions[3], positions[4] = positions[3], positions[3], positions[2], positions[2]
#         else:
#             positions[1], positions[2], positions[3], positions[4] = positions[3], positions[3], positions[3] + 1, positions[2]
#     else:
#         if two_indexes_equal:
#             positions[2], positions[3], positions[4] = positions[3], positions[2], positions[2]
#         else:
#             positions[2], positions[3], positions[4] = positions[3], positions[3] + 1, positions[2]
#
# class Solution:
#     def sortColors(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         positions = [-1, -1, -1, -1, -1] # last index of 0, first index of 1, last index of 1, first index of 2 and last index of 2
#
#         for idx in range(len(nums)):
#             num = nums[idx]
#
#             if num == 0:
#                 positions[0] = idx
#             elif num == 1:
#                 if positions[1] == -1:
#                     positions[1] = idx
#                 positions[2] = idx
#             elif num == 2:
#                 if positions[3] == -1:
#                     positions[3] = idx
#                 positions[4] = idx
#
#             # make sure 0 is before 1 or 2
#             if positions[0] != -1:
#                 if positions[1] != -1 and positions[0] > positions[1]:
#                     move_zero_before_one(nums, positions)
#                 elif positions[3] != -1 and positions[0] > positions[3]:
#                     move_zero_before_two(nums, positions)
#
#             # make sure 1 is before 2
#             if positions[2] != -1:
#                 if positions[4] != -1 and positions[4] < positions[2]:
#                     move_one_before_two(nums, positions)

# -----------------------------------------
# Enhanced Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        start = 0
        end   = len(nums) - 1
        index = 0
        while index <= end and start < end:
            if nums[index] == 0:
                nums[index], nums[start] = nums[start], 0
                start += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[end] = nums[end], 2
                end -= 1
