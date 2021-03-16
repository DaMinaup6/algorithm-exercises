# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeros = []
        for num in nums:
            if num != 0:
                non_zeros.append(num)

        for index in range(len(nums)):
            if index < len(non_zeros):
                nums[index] = non_zeros[index]
            else:
                nums[index] = 0

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/coder_orz/article/details/51384498
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cursor = 0
        for num in nums:
            if num != 0:
                nums[cursor] = num
                cursor += 1

        for index in range(cursor, len(nums)):
            nums[index] = 0

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/coder_orz/article/details/51384498
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1
