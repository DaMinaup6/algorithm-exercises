# -----------------------------------------
# My Solution: Two Pointers
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest_sum = float('inf')
        for index in range(len(nums) - 2):
            if index > 0 and nums[index - 1] == nums[index]:
                continue

            curr_num = nums[index]
            left_pointer, right_pointer = index + 1, len(nums) - 1
            while left_pointer < right_pointer:
                curr_sum = curr_num + nums[left_pointer] + nums[right_pointer]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return target
                elif curr_sum > target:
                    right_pointer -= 1
                else:
                    left_pointer += 1
        return closest_sum
