# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/find-peak-element/solution/
# b)https://youtu.be/HtSuA80QTyo?t=1660
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] > nums[middle_pointer + 1]:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer + 1
        return left_pointer
