# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(6n)
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i][j][k] := how many possible attendance records with record length i, j absent records and k consecutive late days
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[1][0][0] = dp[1][1][0] = dp[1][0][1] = 1
        for curr_day in range(2, n + 1):
            # curr_record == 'P'
            for absent_days in [0, 1]:
                for late_days in [0, 1, 2]:
                    dp[curr_day][absent_days][0] = (dp[curr_day][absent_days][0] + dp[curr_day - 1][absent_days][late_days]) % MOD
            # curr_record == 'A'
            for late_days in [0, 1, 2]:
                dp[curr_day][1][0] = (dp[curr_day][1][0] + dp[curr_day - 1][0][late_days]) % MOD
            # curr_record == 'L'
            for absent_days in [0, 1]:
                for late_days in [1, 2]:
                    dp[curr_day][absent_days][late_days] = (dp[curr_day][absent_days][late_days] + dp[curr_day - 1][absent_days][late_days - 1]) % MOD

        return sum(sum(dp[-1], [])) % MOD

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        curr_dp = [[0] * 3 for _ in range(2)]
        curr_dp[0][0] = curr_dp[1][0] = curr_dp[0][1] = 1
        for curr_day in range(2, n + 1):
            next_dp = [[0] * 3 for _ in range(2)]
            # curr_record == 'P'
            for absent_days in [0, 1]:
                for late_days in [0, 1, 2]:
                    next_dp[absent_days][0] = (next_dp[absent_days][0] + curr_dp[absent_days][late_days]) % MOD
            # curr_record == 'A'
            for late_days in [0, 1, 2]:
                next_dp[1][0] = (next_dp[1][0] + curr_dp[0][late_days]) % MOD
            # curr_record == 'L'
            for absent_days in [0, 1]:
                for late_days in [1, 2]:
                    next_dp[absent_days][late_days] = (next_dp[absent_days][late_days] + curr_dp[absent_days][late_days - 1]) % MOD

            curr_dp = next_dp

        return sum(sum(curr_dp, [])) % MOD

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        curr_dp = [[0] * 3 for _ in range(2)]
        curr_dp[0][0] = curr_dp[1][0] = curr_dp[0][1] = 1
        for curr_day in range(2, n + 1):
            next_dp = [[0] * 3 for _ in range(2)]
            next_dp[0][0] = sum(curr_dp[0][late_days] for late_days in [0, 1, 2]) % MOD
            next_dp[1][0] = sum(curr_dp[absent_days][late_days] for absent_days in [0, 1] for late_days in [0, 1, 2]) % MOD
            next_dp[0][1] = curr_dp[0][0]
            next_dp[0][2] = curr_dp[0][1]
            next_dp[1][1] = curr_dp[1][0]
            next_dp[1][2] = curr_dp[1][1]

            curr_dp = next_dp

        return sum(sum(curr_dp, [])) % MOD

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/student-attendance-record-ii/discuss/101655/Python-O(N)-solution
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # P   := dp[0][0]
        # A   := dp[1][0]
        # L   := dp[0][1]
        # LL  := dp[0][2]
        # AL  := dp[1][1]
        # ALL := dp[1][2]
        P, A, L, LL, AL, ALL = 1, 1, 1, 0, 0, 0
        for _ in range(2, n + 1):
            P, A, L, LL, AL, ALL = sum((P, L, LL)) % MOD, sum((P, A, L, LL, AL, ALL)) % MOD, P, L, A, AL
        return sum((P, A, L, LL, AL, ALL)) % MOD
