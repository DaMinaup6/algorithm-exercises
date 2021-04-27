# -----------------------------------------
# My Solution: Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left_pointer, right_pointer = 0, 1
        while right_pointer < len(nums):
            if nums[right_pointer] > nums[left_pointer]:
                left_pointer += 1
                nums[left_pointer] = nums[right_pointer]
            right_pointer += 1

        return left_pointer + 1
