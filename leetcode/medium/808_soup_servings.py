# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
import math

class Solution:
    def soupServings(self, n: int) -> float:
        # Answers within 10-6 of the true value will be accepted as correct.
        # for n > 4800 the answers are all 1.00000
        if n > 4800:
            return 1.0

        # the unit of this problem is 25
        n = math.ceil(n / 25)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for soup_vol in range(1, n + 1):
            dp[0][soup_vol] = 1

        for soup_vol_a in range(1, n + 1):
            for soup_vol_b in range(1, n + 1):
                dp[soup_vol_a][soup_vol_b] += 0.25 * dp[max(soup_vol_a - 4, 0)][soup_vol_b]
                dp[soup_vol_a][soup_vol_b] += 0.25 * dp[max(soup_vol_a - 3, 0)][max(soup_vol_b - 1, 0)]
                dp[soup_vol_a][soup_vol_b] += 0.25 * dp[max(soup_vol_a - 2, 0)][max(soup_vol_b - 2, 0)]
                dp[soup_vol_a][soup_vol_b] += 0.25 * dp[max(soup_vol_a - 1, 0)][max(soup_vol_b - 3, 0)]
        return dp[-1][-1]
