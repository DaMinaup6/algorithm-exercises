# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        i = 0
        j = None
        for index in range(1, len(nums)):
            num = nums[index]
            if num < nums[i]:
                i = index
            elif j is None and num > nums[i]:
                j = index
            elif j is not None:
                if num > nums[j]:
                    return True
                elif nums[i] < num < nums[j]:
                    j = index

        return False

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79826703
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
