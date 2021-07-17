# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(arr)
from collections import defaultdict

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        if all(num == 0 for num in arr):
            return [0, 2]

        bin_range_sum = [0]
        for num in arr:
            bin_range_sum.append(bin_range_sum[-1] * 2 + num)
        def bin_num_between(left, right):
            return bin_range_sum[right + 1] - bin_range_sum[left] * pow(2, right - left + 1)

        num_from_left_index = defaultdict(int)
        num_from_left = 0
        for index in range(len(arr) - 2):
            num_from_left = num_from_left * 2 + arr[index]
            num_from_left_index[num_from_left] = index

        num_from_right_index = defaultdict(int)
        num_from_right = 0
        for index in range(len(arr) - 1, 1, -1):
            if arr[index] == 0:
                continue
            num_from_right += pow(2, len(arr) - 1 - index)
            num_from_right_index[num_from_right] = index

        for bin_num in num_from_left_index:
            if bin_num not in num_from_right_index or num_from_left_index[bin_num] + 1 >= num_from_right_index[bin_num]:
                continue

            right_position = num_from_right_index[bin_num]
            while num_from_left_index[bin_num] + 1 < right_position:
                if bin_num_between(num_from_left_index[bin_num] + 1, right_position - 1) == bin_num:
                    return [num_from_left_index[bin_num], right_position]

                right_position -= 1
                if arr[right_position] == 1:
                    break
        return [-1, -1]

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(arr)
#
# Ref: https://leetcode.com/problems/three-equal-parts/solution/
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones_count = sum(arr)
        if ones_count == 0:
            return [0, 2] # len(arr) >= 3 is guaranteed in problem description
        if ones_count % 3 != 0:
            return [-1, -1]

        each_part_ones_count = ones_count // 3
        curr_ones_count = 0
        part_1_first_one_index = -1
        part_1_last_one_index  = -1
        part_2_first_one_index = -1
        part_2_last_one_index  = -1
        part_3_first_one_index = -1
        part_3_last_one_index  = -1
        for index, num in enumerate(arr):
            if num == 1:
                curr_ones_count += 1
                if curr_ones_count == 1:
                    part_1_first_one_index = index
                if curr_ones_count == each_part_ones_count:
                    part_1_last_one_index = index
                if curr_ones_count == each_part_ones_count + 1:
                    part_2_first_one_index = index
                if curr_ones_count == each_part_ones_count * 2:
                    part_2_last_one_index = index
                if curr_ones_count == each_part_ones_count * 2 + 1:
                    part_3_first_one_index = index
                if curr_ones_count == each_part_ones_count * 3:
                    part_3_last_one_index = index
        if not arr[part_1_first_one_index:(part_1_last_one_index + 1)] == arr[part_2_first_one_index:(part_2_last_one_index + 1)] == arr[part_3_first_one_index:(part_3_last_one_index + 1)]:
            return [-1, -1]

        part_3_tail_zeros_count = len(arr) - part_3_last_one_index - 1
        part_1_zeros_after_last_one_count = part_2_first_one_index - part_1_last_one_index - 1
        part_2_zeros_after_last_one_count = part_3_first_one_index - part_2_last_one_index - 1
        # extra zeros after last one can be put in front of next part as leading zeros
        if part_1_zeros_after_last_one_count < part_3_tail_zeros_count or part_2_zeros_after_last_one_count < part_3_tail_zeros_count:
            return [-1, -1]
        return [part_1_last_one_index + part_3_tail_zeros_count, part_2_last_one_index + part_3_tail_zeros_count + 1]
