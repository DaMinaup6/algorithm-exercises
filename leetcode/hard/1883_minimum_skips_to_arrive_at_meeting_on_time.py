# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1239772/Python-dp-O(n2)
import sys
import math

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        # dp[i][j] := minimum time to travel the roads where i := last road index (1-base) and j := number of skips
        dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        for index, distance in enumerate(dist, 1):
            # use round to eliminate inaccuracies caused by float
            # also note that no need do skip for last road
            dp[index][0] = math.ceil(round(dp[index - 1][0] + distance / speed, 7)) if index < len(dist) else dp[index - 1][0] + distance / speed
            for skips in range(1, index + 1):
                if index < len(dist):
                    do_skip_time = dp[index - 1][skips - 1] + distance / speed
                    no_skip_time = math.ceil(round(dp[index - 1][skips] + distance / speed, 7))
                else:
                    do_skip_time = no_skip_time = dp[index - 1][skips] + distance / speed
                dp[index][skips] = min(do_skip_time, no_skip_time)

        for skips, time in enumerate(dp[-1]):
            if time <= hoursBefore:
                return skips
        return -1
