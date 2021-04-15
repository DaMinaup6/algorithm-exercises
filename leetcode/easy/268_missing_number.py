# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += [-1]
        for index, num in enumerate(nums):
            if num == index or num == -1:
                continue

            curr_num = num
            while nums[index] != index and nums[index] != -1:
                nums[index], nums[curr_num] = nums[curr_num], nums[index]
                curr_num = nums[index]

        return nums.index(-1)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)
        for index, num in enumerate(nums):
            missing_num ^= index ^ num

        return missing_num

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
