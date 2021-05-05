# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        # add one last redundant stair, the min cost of reaching this stair is the answer
        cost.append(0)
        # dp[i] := min cost spend to reach stair i
        dp = [0] * len(cost)
        # skip stair 0 and 1 since the cost to reach these two stairs is 0 (we can start from either stair 0 or stair 1)
        for stair in range(2, len(cost)):
            dp[stair] = min(dp[stair - 1] + cost[stair - 1], dp[stair - 2] + cost[stair - 2])

        return dp[-1]

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        cost.append(0)
        cost_from_floor_0, cost_from_floor_1 = 0, 0
        for stair in range(2, len(cost)):
            curr_cost = min(cost_from_floor_1 + cost[stair - 1], cost_from_floor_0 + cost[stair - 2])

            cost_from_floor_0 = cost_from_floor_1
            cost_from_floor_1 = curr_cost

        return cost_from_floor_1
