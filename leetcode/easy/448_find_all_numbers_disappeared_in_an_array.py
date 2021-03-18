# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared_numbers = set(range(1, len(nums) + 1))
        for num in nums:
            if num in disappeared_numbers:
                disappeared_numbers.remove(num)

        return list(disappeared_numbers)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/53981307
# Note: For space complexity we ignored the output list
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            neg_index = abs(nums[index]) - 1
            nums[neg_index] = -abs(nums[neg_index])

        return [index + 1 for index in range(len(nums)) if nums[index] > 0]
