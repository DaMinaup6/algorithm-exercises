# -----------------------------------------
# Original
# -----------------------------------------
# import copy
#
# def operations_to_target(nums_count, total_diff):
#     operation = 0
#     if total_diff == 0:
#         return 0
#     elif total_diff > 0:
#         for available_num in range(1, 6):
#             if nums_count[available_num] > 0:
#                 for possible_diff in range(6 - available_num, 0, -1):
#                     multiplier  = min(abs(total_diff) // possible_diff, nums_count[available_num])
#                     total_diff -= possible_diff * multiplier
#                     operation  += multiplier
#                     nums_count[available_num] -= multiplier
#
#                     if total_diff <= 0:
#                         return operation
#     elif total_diff < 0:
#         for available_num in range(6, 1, -1):
#             if nums_count[available_num] > 0:
#                 for possible_diff in range(available_num - 1, 0, -1):
#                     multiplier  = min(abs(total_diff) // possible_diff, nums_count[available_num])
#                     total_diff += possible_diff * multiplier
#                     operation  += multiplier
#                     nums_count[available_num] -= multiplier
#
#                     if total_diff >= 0:
#                         return operation
#
#     return None
#
# class Solution:
#     def minOperations(self, nums1, nums2):
#         nums1_sum = sum(nums1)
#         nums2_sum = sum(nums2)
#         if nums1_sum == nums2_sum:
#             return 0
#
#         nums1_min = len(nums1)
#         nums1_max = len(nums1) * 6
#         nums2_min = len(nums2)
#         nums2_max = len(nums2) * 6
#         if nums1_min > nums2_max or nums2_min > nums1_max:
#             return -1
#
#         nums1_count = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
#         nums2_count = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
#         for num in nums1:
#             nums1_count[num] += 1
#         for num in nums2:
#             nums2_count[num] += 1
#
#         operations = []
#         for target in range(max(nums1_min, nums2_min), min(nums1_max, nums2_max) + 1):
#             operation_1 = operations_to_target(copy.copy(nums1_count), target - nums1_sum)
#             if operation_1 is None:
#                 continue
#             operation_2 = operations_to_target(copy.copy(nums2_count), target - nums2_sum)
#             if operation_2 is None:
#                 continue
#             operations.append(operation_1 + operation_2)
#
#         return -1 if len(operations) == 0 else min(operations)

# -----------------------------------------
# Greedy
# -----------------------------------------
import math

class Solution:
    def minOperations(self, nums1, nums2):
        nums1_sum = 0
        nums2_sum = 0
        nums1_count = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
        nums2_count = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
        for num in nums1:
            nums1_sum += num
            nums1_count[num] += 1
        for num in nums2:
            nums2_sum += num
            nums2_count[num] += 1

        if nums1_sum == nums2_sum:
            return 0

        nums1_min = len(nums1)
        nums1_max = len(nums1) * 6
        nums2_min = len(nums2)
        nums2_max = len(nums2) * 6
        if nums1_min > nums2_max or nums2_min > nums1_max:
            return -1

        larger_nums,  larger_nums_count  = [nums1, nums1_count] if nums1_sum > nums2_sum else [nums2, nums2_count]
        smaller_nums, smaller_nums_count = [nums1, nums1_count] if nums1_sum < nums2_sum else [nums2, nums2_count]
        total_diff = abs(nums1_sum - nums2_sum)
        operations = 0
        for num in range(1, 6):
            if total_diff <= 0:
                break

            if larger_nums_count[7 - num] > 0 and total_diff > 0:
                operation   = min(math.ceil(total_diff / (6 - num)), larger_nums_count[7 - num])
                total_diff -= (6 - num) * operation
                operations += operation
                larger_nums_count[7 - num] -= operation

            if smaller_nums_count[num] > 0 and total_diff > 0:
                operation   = min(math.ceil(total_diff / (6 - num)), smaller_nums_count[num])
                total_diff -= (6 - num) * operation
                operations += operation
                smaller_nums_count[num] -= operation

        return operations if total_diff <= 0 else -1

solution = Solution()
print(f"01. solution.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]) ==  3: {solution.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]) == 3}")
print(f"02. solution.minOperations([1, 1, 1, 1, 1, 1, 1], [6])             == -1: {solution.minOperations([1, 1, 1, 1, 1, 1, 1], [6]) == -1}")
print(f"03. solution.minOperations([6, 6], [1])                            ==  3: {solution.minOperations([6, 6], [1]) == 3}")
