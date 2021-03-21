# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/L141210113/article/details/88306238
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 else 1

        dividend = abs(dividend)
        divisor  = abs(divisor)
        result   = 0
        while dividend >= divisor:
            shift_bits = 0
            while dividend >= divisor << (shift_bits + 1):
                shift_bits += 1
            dividend -= divisor << shift_bits
            result += 1 << shift_bits
        result *= flag

        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result
