# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/wiggle-sort-ii/discuss/962127/Sort-solution
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = list(sorted(nums))
        
        for index in range(1, len(nums), 2):
            nums[index] = sorted_nums.pop()
        for index in range(0, len(nums), 2):
            nums[index] = sorted_nums.pop()
