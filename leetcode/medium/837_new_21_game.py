# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/83615241
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or W == 1:
            return 1.0

        # dp[i] := probability of gettint point i
        # possible max score is K + W - 1 and it's no need to calculate probability of getting point more than N
        max_point = min(K + W - 1, N)
        dp = [0] * (max_point + 1)
        dp[0] = 1.0

        prev_w_dp_sum = dp[0]
        for point in range(1, max_point + 1):
            # e.g. W == 10, dp[15] == dp[5] * (1 / W) + dp[6] * (1 / W) + ... + dp[14] * (1 / W) == (dp[5] + dp[6] + ... + dp[14]) / W
            #                                    ^                 ^                        ^                         ^
            #                                    |                 |                        |                         |
            #                              prob get 10       prob get 9               prob get 1                total W terms
            dp[point] = prev_w_dp_sum / W
            # e.g. N == 21, K == 17, W == 10, dp[20] == dp[10] * (1 / W) + dp[11] * (1 / W) + ... + dp[16] * (1 / W)
            #                                                       ^                  ^                        ^
            #                                                       |                  |                        |
            #                                                 prob get 10        prob get 9               prob get 4
            # there would be no probability like dp[17] + (probability of getting 3) since once Alick gets points >= K she just stops drawing
            if point < K:
                prev_w_dp_sum += dp[point]
            if W <= point:
                prev_w_dp_sum -= dp[point - W]

        return sum(dp[K:])
