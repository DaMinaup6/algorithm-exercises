# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^m)
# Space Complexity: O(n^m)
# -----------------------------------------
# Note: This solution leads to TLE
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        min_cost = float('inf')

        def dfs(curr_house_index, curr_cost, curr_neighborhoods):
            nonlocal min_cost

            if curr_neighborhoods > target:
                return
            if curr_house_index == m:
                if curr_neighborhoods == target:
                    min_cost = min(min_cost, curr_cost)
                return

            if houses[curr_house_index] != 0:
                next_neighborhoods = curr_neighborhoods
                if curr_house_index == 0 or houses[curr_house_index] != houses[curr_house_index - 1]:
                    next_neighborhoods += 1
                dfs(curr_house_index + 1, curr_cost, next_neighborhoods)
            else:
                for color in range(1, n + 1):
                    houses[curr_house_index] = color
                    next_neighborhoods = curr_neighborhoods
                    if curr_house_index == 0 or houses[curr_house_index] != houses[curr_house_index - 1]:
                        next_neighborhoods += 1
                    dfs(curr_house_index + 1, curr_cost + cost[curr_house_index][color - 1], next_neighborhoods)
                    houses[curr_house_index] = 0

        dfs(0, 0, 0)
        return min_cost if min_cost != float('inf') else -1

# -----------------------------------------
# Model Solution: Dynamic Programing
#
# Time  Complexity: O(mt * n^2)
# Space Complexity: O(mnt)
# -----------------------------------------
# Ref: https://blog.csdn.net/Changxing_J/article/details/112522365
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][j][k] := the min cost at house position i with color j of previous house and k neighborhoods
        dp = [[[-1] * (target + 1) for _ in range(n)] for _ in range(m)]

        if houses[0] == 0:
            for j in range(n):
                dp[0][j][1] = cost[0][j]
        else:
            j = houses[0] - 1 # color is 1-based but for dp the color index is 0-based so need minus 1 here
            dp[0][j][1] = 0

        for curr_house_index in range(1, m):
            if houses[curr_house_index] == 0:
                for curr_color in range(n):
                    for curr_neighborhoods in range(1, target + 1):
                        for prev_color in range(n):
                            if prev_color == curr_color:
                                if dp[curr_house_index - 1][prev_color][curr_neighborhoods] != -1:
                                    if dp[curr_house_index][curr_color][curr_neighborhoods] == -1 or dp[curr_house_index - 1][prev_color][curr_neighborhoods] + cost[curr_house_index][curr_color] < dp[curr_house_index][curr_color][curr_neighborhoods]:
                                        dp[curr_house_index][curr_color][curr_neighborhoods] = dp[curr_house_index - 1][prev_color][curr_neighborhoods] + cost[curr_house_index][curr_color]
                            else:
                                if dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1] != -1:
                                    if dp[curr_house_index][curr_color][curr_neighborhoods] == -1 or dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1] + cost[curr_house_index][curr_color] < dp[curr_house_index][curr_color][curr_neighborhoods]:
                                        dp[curr_house_index][curr_color][curr_neighborhoods] = dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1] + cost[curr_house_index][curr_color]
            else:
                curr_color = houses[curr_house_index] - 1
                for curr_neighborhoods in range(1, target + 1):
                    for prev_color in range(n):
                        if prev_color == curr_color:
                            if dp[curr_house_index - 1][prev_color][curr_neighborhoods] != -1:
                                if dp[curr_house_index][curr_color][curr_neighborhoods] == -1 or dp[curr_house_index - 1][prev_color][curr_neighborhoods] < dp[curr_house_index][curr_color][curr_neighborhoods]:
                                    dp[curr_house_index][curr_color][curr_neighborhoods] = dp[curr_house_index - 1][prev_color][curr_neighborhoods]
                        else:
                            if dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1] != -1:
                                if dp[curr_house_index][curr_color][curr_neighborhoods] == -1 or dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1] < dp[curr_house_index][curr_color][curr_neighborhoods]:
                                    dp[curr_house_index][curr_color][curr_neighborhoods] = dp[curr_house_index - 1][prev_color][curr_neighborhoods - 1]

        ans = [dp[-1][j][-1] for j in range(n) if dp[-1][j][-1] != -1]
        return min(ans) if len(ans) > 0 else -1
