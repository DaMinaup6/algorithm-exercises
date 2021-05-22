# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nk)
# Space Complexity: O(1)
# -----------------------------------------
# k := time complexity of removing element from list
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == val:
                nums.pop(pointer)
            else:
                pointer += 1
        return len(nums)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/remove-element/solution/197569
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for index in range(len(nums)):
            if nums[index] != val :
                nums[count] = nums[index]
                count += 1
        return count
