# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^(1.5))
# Space Complexity: O(n)
# -----------------------------------------
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        for num in range(1, n + 1):
            closest_square_root = int(math.sqrt(num))
            if num == closest_square_root * closest_square_root:
                dp[num] = 1
            else:
                for square_root in range(1, closest_square_root + 1):
                    square  = square_root * square_root
                    dp[num] = min(dp[num], dp[square] + dp[num - square])

        return dp[n]
