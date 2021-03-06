# -----------------------------------------
# O(n^2): My Solution
# -----------------------------------------
# class Solution:
#     def canJump(self, nums):
#         # nums is non-negative integers array
#         cursor = 0
#         target_index = len(nums) - 1
#
#         while cursor <= target_index:
#             jump_cap = nums[cursor]
#             if cursor + jump_cap >= target_index:
#                 return True
#             elif jump_cap == 0:
#                 return False
#
#             farest_index = cursor + 1
#             next_cursor  = cursor + 1
#             for landing_index in range(cursor + 1, cursor + 1 + jump_cap):
#                 if landing_index + nums[landing_index] >= farest_index:
#                     farest_index = landing_index + nums[landing_index]
#                     next_cursor  = landing_index
#             cursor = next_cursor
#
#         return False

# -----------------------------------------
# O(n): Greddy
# -----------------------------------------
class Solution:
    def canJump(self, nums):
        # nums is non-negative integers array
        last_index = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= last_index:
                last_index = index

        return last_index == 0
