# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n + log(n))
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return float('inf')
        if len(nums) == 1:
            return nums[0]

        left  = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] != nums[left]:
                right = middle
            else:
                nums_1 = nums[left:(middle + 1)]
                nums_2 = nums[(middle + 1):(right + 1)]
                return min(self.findMin(nums_1), self.findMin(nums_2))

        return nums[left]

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://maxming0.github.io/2020/07/25/Find-Minimum-in-Rotated-Sorted-Array-II/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] != nums[left]:
                right = middle
            else:
                right -= 1

        return nums[left]
