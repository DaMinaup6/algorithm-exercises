# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        keep = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)
        keep[0] = -prices[0]
        for index in range(1, len(prices)):
            keep[index] = max(rest[index - 1] - prices[index], keep[index - 1])
            sell[index] = keep[index - 1] + prices[index]
            rest[index] = max(rest[index - 1], sell[index - 1])
        return max(sell[len(prices) - 1], rest[len(prices) - 1])

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/zjuPeco/article/details/76468185
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        curr_keep = -prices[0]
        curr_sell = 0
        curr_rest = 0
        for index in range(1, len(prices)):
            prev_keep = curr_keep
            prev_sell = curr_sell
            prev_rest = curr_rest

            curr_keep = max(prev_rest - prices[index], prev_keep)
            curr_sell = prev_keep + prices[index]
            curr_rest = max(prev_rest, prev_sell)
        return max(curr_sell, curr_rest)

# -----------------------------------------
# At most k transactions
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=oDhu5uGq_ic
class Solution:
    def maxProfit(self, k, prices: List[int]) -> int: # for problem 309 k would be math.ceil(len(prices) / 2)
        if len(prices) < 2:
            return 0

        # i := transaction, j := day, dp[i][j] := maximum profit can make in i-th transaction at j-th day
        dp = [[0] * len(prices) for _ in range(k + 1)]
        # TODO: enhance time and space complexity
        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                dp[i][j] = max(
                    dp[i][j - 1],
                    # just like in problem 188, but when buy at day k, we can only use max profit from k - 2 day since there is a one day cooldown
                    prices[j] + max(dp[i - 1][k - 2] - prices[k] if k >= 2 else -prices[k] for k in range(j)),
                )
        return dp[k][len(prices) - 1]
