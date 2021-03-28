# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://stackoverflow.com/a/25905474
class Solution:
    def minSteps(self, n: int) -> int:
        dp = list(range(n + 1))
        dp[1] = 0        
        for num in range(2, n + 1):
            multiplier = 2
            while num * multiplier <= n:
                next_num = num * multiplier
                # copy and paste == (dp[num] + 1) + (multiplier - 1)
                # e.g. AA -> AAAAAA, copy AA (dp[2] + 1) + paste AA 2 times (multiplier - 1)
                dp[next_num] = min(dp[next_num], dp[num] + multiplier)
                multiplier += 1

        return dp[n]
