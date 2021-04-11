# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left  = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if middle < len(nums) - 1 and nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            if middle > 0 and nums[middle] < nums[middle - 1]:
                return nums[middle]

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return nums[left - 1]

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/236652
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1

        return nums[left]
