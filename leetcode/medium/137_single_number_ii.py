# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(32n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://hanfeng.ink/post/bitwise/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        single_number = 0
        for bit_position in range(32):
            count = 0
            # count 1 bit on bit_position
            for num in nums:
                if (num >> bit_position) & 1 == 1:
                    count += 1
            single_number |= (count % 3) << bit_position

        # if single_number > pow(2, 31), it must be a negative number
        return single_number if single_number < pow(2, 31) else single_number - pow(2, 32)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://hanfeng.ink/post/bitwise/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one_xor = two_xor = 0
        for num in nums:
            one_xor = (one_xor ^ num) & ~two_xor
            two_xor = (two_xor ^ num) & ~one_xor

        return one_xor
