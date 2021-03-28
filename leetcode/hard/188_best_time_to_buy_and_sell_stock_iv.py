# -----------------------------------------
# Dynamic Programming
# -----------------------------------------
# n := len(prices)
# Ref: https://www.youtube.com/watch?v=oDhu5uGq_ic

# -----> Version 1
# Time  Complexity: O(kn^2)
# Space Complexity: O(kn)
# Note: this leads to TLE but easier to understand
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0

        # i := transaction, j := day, dp[i][j] := maximum profit can make in i-th transaction at j-th day
        dp = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max(dp[i - 1][k] - prices[k] for k in range(j)))
        return dp[k][len(prices) - 1]

# -----> Version 2
# Time  Complexity: O(kn)
# Space Complexity: O(kn)
# Note: this is an enhanced solution of previous one
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0

        # i := transaction, j := day, dp[i][j] := maximum profit can make in i-th transaction at j-th day
        dp = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0] # it should be dp[i - 1][0] - prices[0] but dp[i - 1][0] always equals 0 so just ignore it
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(dp[i - 1][j] - prices[j], max_diff)
        return dp[k][len(prices) - 1]

# -----> Version 3
# Time  Complexity: O(kn)
# Space Complexity: O(n)
# Note: reduce space complexity to O(n) since we only need dp[i] and dp[i - 1] for each iteration
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0

        dp_curr = [0] * len(prices)
        for _ in range(1, k + 1):
            max_diff = -prices[0]
            dp_prev  = dp_curr
            dp_curr  = [0] * len(prices) # in previous all dp[i] starts with initial values, so here need to initialize dp_curr at each transaction
            for j in range(1, len(prices)):
                dp_curr[j] = max(dp_curr[j - 1], prices[j] + max_diff)
                max_diff   = max(dp_prev[j] - prices[j], max_diff)
        return dp_curr[len(prices) - 1]

# -----------------------------------------
# Dynamic Programming
#
# Time  Complexity: O(kn)
# Space Complexity: O(k)
# -----------------------------------------
# n := len(prices)
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0

        buy  = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for transaction in range(1, k + 1):
                buy[transaction]  = max(buy[transaction], sell[transaction - 1] - price)
                sell[transaction] = max(sell[transaction], buy[transaction] + price)
        return sell[k]
