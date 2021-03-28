# -----------------------------------------
# My Solution: DP
#
# Time  Complexity: O(mn)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(coins), n := amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_set = set(coins)

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for sub_amount in range(1, amount + 1):
            if sub_amount in coin_set:
                dp[sub_amount] = 1
            else:
                for coin in coin_set:
                    if coin > sub_amount or dp[coin] == -1 or dp[sub_amount - coin] == -1:
                        continue

                    new_num = dp[coin] + dp[sub_amount - coin]
                    if dp[sub_amount] == -1:
                        dp[sub_amount] = new_num
                    else:
                        dp[sub_amount] = min(dp[sub_amount], new_num)

        return dp[amount]

# -----------------------------------------
# Dynamic Programming (Knapsack Problem)
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(coins), n := amount
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for sub_amount in range(coin, amount + 1):
                dp[sub_amount] = min(dp[sub_amount], dp[sub_amount - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# -----------------------------------------
# DFS + Greedy + Pruning
#
# Time  Complexity: O((n / coin_0) * (n / coin_1) * ... * (n / coin_(m - 1)))
# Space Complexity: O(m)
# -----------------------------------------
# m := len(coins), n := amount
# Ref: https://youtu.be/uUETHdijzkA?t=905
class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)

        coin_num = float('inf')
        def dfs(coin_index, amount, current_coin_num):
            nonlocal coin_num

            if amount == 0:
                coin_num = current_coin_num
                return
            if coin_index == len(coins):
                return
            
            coin = coins[coin_index]
            for multiplier in range(amount // coin, -1, -1):
                if current_coin_num + multiplier >= coin_num:
                    break
                dfs(coin_index + 1, amount - multiplier * coin, current_coin_num + multiplier)

        dfs(0, amount, 0)
        return -1 if coin_num == float('inf') else coin_num
