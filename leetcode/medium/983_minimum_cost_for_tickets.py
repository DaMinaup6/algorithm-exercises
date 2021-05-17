# -----------------------------------------
# My Solution: Dynamic Programming + Binary Search
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(days)
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (len(days) + 1)
        dp[0] = 0
        for curr_day_index in range(len(days)):
            # cost of using 1-day pass
            dp[curr_day_index + 1] = min(dp[curr_day_index + 1], dp[curr_day_index] + costs[0])
            # cost of using 7-day pass
            next_day_index = bisect.bisect_left(days, days[curr_day_index] + 7, curr_day_index)
            dp[next_day_index] = min(dp[next_day_index], dp[curr_day_index] + costs[1])
            # cost of using 30-day pass
            next_day_index = bisect.bisect_left(days, days[curr_day_index] + 30, curr_day_index)
            dp[next_day_index] = min(dp[next_day_index], dp[curr_day_index] + costs[2])

        return dp[-1]
