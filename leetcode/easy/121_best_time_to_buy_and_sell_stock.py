# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        buy_cursor = 0

        for index in range(1, len(prices)):
            profit = prices[index] - prices[buy_cursor]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy_cursor = index

        return max_profit
