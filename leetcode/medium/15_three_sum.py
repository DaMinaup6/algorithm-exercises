# -----------------------------------------
# My Solution: Three Pointers
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
# Note: If output considered in space complexity then it takes O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output  = set()
        pointer = 1
        while pointer <= len(nums) - 2:
            prev_pointer, next_pointer = pointer - 1, pointer + 1
            while prev_pointer >= 0 and next_pointer < len(nums):
                curr_sum = nums[prev_pointer] + nums[pointer] + nums[next_pointer]
                if curr_sum == 0:
                    output.add((nums[prev_pointer], nums[pointer], nums[next_pointer]))
                    prev_pointer -= 1
                    next_pointer += 1
                elif curr_sum > 0:
                    prev_pointer -= 1
                else:
                    next_pointer += 1
            pointer += 1
        return output

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = set()
        for index, num_1 in enumerate(nums[:-2]):
            if index >= 1 and num_1 == nums[index - 1]:
                continue

            temp_dict = set()
            for num_2 in nums[(index + 1):]:
                # if num_2 already in temp_dict, then it must be added by other_num such that -(num_1 + other_num) == num_2 => other_num == -(num_1 + num_2)
                # so other_num exists
                if num_2 not in temp_dict:
                    temp_dict.add(-(num_1 + num_2))
                else:
                    output.add((num_1, num_2, -(num_1 + num_2)))
        return output
