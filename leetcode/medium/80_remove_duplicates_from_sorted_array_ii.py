# -----------------------------------------
# My Solution: Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        left_pointer, right_pointer = 0, 1
        curr_duplicated = False
        while right_pointer < len(nums):
            if curr_duplicated == False and nums[right_pointer] == nums[left_pointer] or nums[right_pointer] > nums[left_pointer]:
                left_pointer += 1
                nums[left_pointer] = nums[right_pointer]
            curr_duplicated = nums[left_pointer] == nums[left_pointer - 1]
            right_pointer += 1

        return left_pointer + 1
