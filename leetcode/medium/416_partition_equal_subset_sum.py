# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(ns)
# Space Complexity: O(s)
# -----------------------------------------
# n := len(nums), s := sum(nums)
# Ref: http://bookshadow.com/weblog/2016/10/09/leetcode-partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        target = nums_sum // 2
        possible_sum_set = set([0])
        for num in nums:
            for possible_sum in possible_sum_set.copy():
                new_possible_sum = possible_sum + num
                if new_possible_sum == target:
                    return True
                elif new_possible_sum > target:
                    continue

                possible_sum_set.add(new_possible_sum)

        return False
