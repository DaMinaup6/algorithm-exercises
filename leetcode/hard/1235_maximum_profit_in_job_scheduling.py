# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(profit)
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_start_time_with_end_time_and_index = sorted([(time, endTime[index], index) for index, time in enumerate(startTime)])
        sorted_start_times = [time for time, _, _ in sorted_start_time_with_end_time_and_index]

        # dp[i] := the max profit we can make from sorted_start_times[i]
        dp = [0] * len(profit)
        def dfs(index):
            if index >= len(profit):
                return 0
            if dp[index] > 0:
                return dp[index]

            _, end_time, profit_index = sorted_start_time_with_end_time_and_index[index]
            first_next_start_time_index = bisect.bisect_left(sorted_start_times, end_time, index + 1)

            dp[index] = profit[profit_index] + max_val_between(first_next_start_time_index, len(profit) - 1)
            return dp[index]

        @lru_cache(None)
        def max_val_between(start_index, end_index):
            if start_index > end_index:
                return 0
            if start_index == end_index:
                return dfs(start_index)
            return max(dfs(start_index), max_val_between(start_index + 1, end_index))

        return max_val_between(0, len(profit) - 1)

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(profit)
#
# Ref: https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1430330/Python-dp-%2B-binary-search-explained
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_start_time_with_end_time_and_index = sorted([(time, endTime[index], profit[index]) for index, time in enumerate(startTime)])
        sorted_start_times = [time for time, _, _ in sorted_start_time_with_end_time_and_index]

        # dp[i] := the max profit we can make from sorted_start_times[i]
        dp = [0] * (len(profit) + 1)
        for index in range(len(profit) - 1, -1, -1):
            _, curr_end_time, curr_profit = sorted_start_time_with_end_time_and_index[index]

            next_start_time_index = bisect.bisect_left(sorted_start_times, curr_end_time)
            dp[index] = max(curr_profit + dp[next_start_time_index], dp[index + 1])

        return dp[0]
