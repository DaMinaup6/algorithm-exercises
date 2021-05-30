# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://stackoverflow.com/a/25905474
class Solution:
    def minSteps(self, n: int) -> int:
        # dp[i] := min operations to get string with length n
        # initialize dp with list(range(n + 1)) is the max operation need for each length
        # e.g. n == 5, copy original character and paste 4 times would get string with length 5,
        #      this taks 5 operations
        dp = list(range(n + 1))
        dp[1] = 0

        # we already consider paste 1 character for each length, so we start from 2 characters
        for num in range(2, n + 1):
            multiplier = 2
            # count operations for pasting string with length num for (multiplier - 1) times
            # string length after pasting equals num + num * (multiplier - 1) == num * multiplier
            # since copy takes 1 operation, paste takes 1 operation so for pasting 1 time, dp[next_num] == dp[num] + 2
            # e.g. num == 2, which means current string == "AA"
            # copy "AA" takes 1 operation, paste "AA" takes 1 string so dp[4] == min(dp[4], dp[2] + 2)
            # then paste "AA" one more time to get "AAAAAA", dp[6] == min(dp[6], dp[2] + 3)
            while num * multiplier <= n:
                next_num = num * multiplier
                dp[next_num] = min(dp[next_num], dp[num] + multiplier)
                multiplier += 1
        return dp[n]
