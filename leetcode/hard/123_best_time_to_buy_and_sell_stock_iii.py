# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # interval_1_max_profits[i] := max profit can make in prices[:(i + 1)]
        interval_1_max_profits = [0] * len(prices)
        interval_1_max_profits[1] = prices[1] - prices[0] if prices[1] > prices[0] else 0
        left_pointer, right_pointer = 0, 2
        if prices[1] <= prices[0]:
            left_pointer = 1
        while right_pointer < len(prices):
            curr_profit = prices[right_pointer] - prices[left_pointer]
            interval_1_max_profits[right_pointer] = max(interval_1_max_profits[right_pointer - 1], curr_profit)
            if curr_profit <= 0:
                left_pointer = right_pointer
            right_pointer += 1

        # interval_2_max_profits[j] := max profit can make in prices[j:]
        interval_2_max_profits = [0] * len(prices)
        interval_2_max_profits[-2] = prices[-1] - prices[-2] if prices[-1] > prices[-2] else 0
        left_pointer, right_pointer = len(prices) - 3, len(prices) - 1
        if prices[-2] >= prices[-1]:
            right_pointer = len(prices) - 2
        while left_pointer >= 0:
            curr_profit = prices[right_pointer] - prices[left_pointer]
            interval_2_max_profits[left_pointer] = max(interval_2_max_profits[left_pointer + 1], curr_profit)
            if curr_profit <= 0:
                right_pointer = left_pointer
            left_pointer -= 1

        max_profit = max(0, interval_2_max_profits[0])
        for index in range(1, len(prices)):
            max_profit = max(max_profit, interval_1_max_profits[index - 1] + interval_2_max_profits[index])

        return max_profit

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=ykQ6WFuqQfE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2 # allowed to complete at most k transactions
        low_prices = [float('inf')] * k
        profits = [0] * k

        for price in prices:
            for index in range(k):
                if index == 0:
                    low_prices[0] = min(low_prices[0], price)
                    profits[0] = max(profits[0], price - low_prices[0])
                else:
                    low_prices[index] = min(low_prices[index], price - profits[index - 1])
                    profits[index] = max(profits[index], price - low_prices[index])
        return profits[-1]
