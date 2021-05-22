# -----------------------------------------
# My Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem./85299
class Solution:
    def integerBreak(self, n: int) -> int:
        # two special cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        # strategy: use as many 3 as possible
        mod_num = n % 3
        if mod_num == 0:
            return pow(3, n // 3)
        elif mod_num == 1:
            return pow(3, n // 3 - 1) * 4
        else:
            return pow(3, n // 3) * 2
