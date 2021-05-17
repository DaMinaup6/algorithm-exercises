# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
# n := len(stones)
# Ref: https://leetcode.com/problems/last-stone-weight-ii/discuss/1200092/python-with-informal-proof
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return max(stones) - min(stones)

        curr_sums = set([0])
        for stone_weight in stones:
            next_sums = set()
            for possible_sum in curr_sums:
                next_sums.update([possible_sum + stone_weight, possible_sum - stone_weight])
            curr_sums = next_sums
        return min([possible_sum for possible_sum in curr_sums if possible_sum >= 0])

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(nw)
# Space Complexity: O(nw)
# -----------------------------------------
# n := len(stones), w := sum(stones)
# Ref: https://leetcode.com/problems/last-stone-weight-ii/discuss/1196755/Python-01-knapsack-solution
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_stone_weight = sum(stones)

        dp = [[0] * (total_stone_weight // 2 + 1) for _ in range(len(stones))]
        for index, stone_weight in enumerate(stones):
            for weight in range(total_stone_weight // 2 + 1):
                if stone_weight <= weight:
                    dp[index][weight] = max(dp[index - 1][weight], dp[index - 1][weight - stone_weight] + stone_weight)
                else:
                    dp[index][weight] = dp[index - 1][weight]
        return total_stone_weight - 2 * dp[-1][-1]
