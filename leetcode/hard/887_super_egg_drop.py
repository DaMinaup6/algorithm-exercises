# -----------------------------------------
# My Solution: DP
#
# Time  Complexity: O(kn^2)
# Space Complexity: O(kn)
# -----------------------------------------
# Note: this solution causes TLE
class Solution:
    def superEggDrop(self, k, n):
        if n == 1:
            return 1
        if k == 1:
            return n

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for index in range(1, k + 1):
            dp[index][1] = 1
            dp[index][2] = 2
        for index in range(1, n + 1):
            dp[1][index] = index
        
        for eggs in range(2, k + 1):
            for floors in range(3, n + 1):
                min_moves = float('inf')
                for floor in range(1, floors):
                    min_moves = min(min_moves, 1 + max(dp[eggs - 1][floor - 1], dp[eggs][floors - floor]))
                dp[eggs][floors] = min_moves

        return dp[k][n]

# -----------------------------------------
# Model Solution: DP + Binary Search
#
# Time  Complexity: O(knlog(n))
# Space Complexity: O(kn)
# -----------------------------------------
# Ref:  https://www.youtube.com/watch?v=aPY6sps_Q44
# Note: this solution causes TLE
class Solution:
    def superEggDrop(self, k, n):
        if n == 1:
            return 1
        if k == 1:
            return n

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for index in range(1, k + 1):
            dp[index][1] = 1
            dp[index][2] = 2
        for index in range(1, n + 1):
            dp[1][index] = index
        
        for eggs in range(2, k + 1):
            for floors in range(3, n + 1):
                left_floor, right_floor = 1, floors
                while left_floor < right_floor:
                    middle_floor = (left_floor + right_floor) // 2
                    if dp[eggs - 1][middle_floor - 1] >= dp[eggs][floors - middle_floor]:
                        right_floor = middle_floor
                    else:
                        left_floor = middle_floor + 1
                dp[eggs][floors] = 1 + max(dp[eggs - 1][left_floor - 1], dp[eggs][floors - left_floor])

        return dp[k][n]

# -----------------------------------------
# Model Solution: DP + Optimality Criterion
#
# Time  Complexity: O(kn)
# Space Complexity: O(kn)
# -----------------------------------------
# Ref: https://www.cnblogs.com/grandyang/p/11048142.html
class Solution:
    def superEggDrop(self, k, n):
        if n == 1:
            return 1
        if k == 1:
            return n

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for index in range(1, k + 1):
            dp[index][1] = 1
            dp[index][2] = 2
        for index in range(1, n + 1):
            dp[1][index] = index
        
        for eggs in range(2, k + 1):
            curr_floor = 1
            for floors in range(3, n + 1):
                while curr_floor < floors and dp[eggs - 1][curr_floor - 1] < dp[eggs][floors - curr_floor]:
                    curr_floor += 1
                dp[eggs][floors] = 1 + max(dp[eggs - 1][curr_floor - 1], dp[eggs][floors - curr_floor])

        return dp[k][n]

# -----------------------------------------
# Model Solution: DP + Optimality Criterion
#
# Time  Complexity: O(kn)
# Space Complexity: O(kn)
# -----------------------------------------
# Ref:  https://www.cnblogs.com/grandyang/p/11048142.html
# TODO: Reduce space complexity
class Solution:
    def superEggDrop(self, k, n):
        if n == 1:
            return 1
        if k == 1:
            return n

        # dp[i][j] := the most number of floors that we can still "solve" with certainty with at most i moves and j eggs
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        curr_move = 0
        while dp[curr_move][k] < n:
            curr_move += 1
            for eggs in range(1, k + 1):
                dp[curr_move][eggs] = dp[curr_move - 1][eggs - 1] + dp[curr_move - 1][eggs] + 1

        return curr_move

# -----------------------------------------
# Model Solution: Mathmatical
#
# Time  Complexity: O(klog(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref:  https://leetcode.com/problems/super-egg-drop/solution/
# TODO: Understand this solution
class Solution:
    def superEggDrop(self, k, n):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, k + 1):
                r *= x - i + 1
                r //= i
                ans += r
                if ans >= n:
                    break
            return ans

        lo, hi = 1, n
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < n:
                lo = mi + 1
            else:
                hi = mi
        return lo
