# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/discuss/1118770/JavaC++Python-Accumulate-the-Coins
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        consecutive_num = 1
        for coin in sorted(coins):
            if coin > consecutive_num:
                break
            consecutive_num += coin

        return consecutive_num
