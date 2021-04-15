# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Note: since there is only 32 bits integers to consider for this problem so time complexity is O(1)
# Ref:
# a) https://www.youtube.com/watch?v=qq64FrA2UXQ
# b) https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # MASK to get last 32 bits since Python won't limit integer to be 32 bit integer

        res, carry = (a ^ b) & MASK, ((a & b) << 1) & MASK
        while carry != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            res, carry = (res ^ carry) & MASK, ((res & carry) << 1) & MASK
        # a is negative if the first bit is 1
        return res if (res >> 31) & 1 == 0 else ~(res ^ MASK)
