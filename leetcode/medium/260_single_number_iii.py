# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/Orientliu96/article/details/103716248
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums

        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1

        num_1, num_2 = 0, 0
        for num in nums:
            if num & mask == 0:
                num_1 ^= num
            else:
                num_2 ^= num
        return [num_1, num_2]
