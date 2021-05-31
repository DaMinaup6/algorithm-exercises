# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # dp[i] := how many numbers with unique digits, these numbers are with i digits
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        # e.g. n == 2
        #      if consider only numbers with 1 digits, there are 9 numbers (from 1 ~ 9)
        #      for each of them, there are 9 choices (i.e. for 1 we got 0, 2, ..., 9) we can put behind it
        #      so we get 9 * 9 == 81 numbers for two digits
        #
        # Hence, for dp[i], the number of it equals (10 - i + 1) * dp[i - 1] since we still have (10 - i + 1) choices after we select (i - 1) distinct digits
        for digits_num in range(2, n + 1):
            dp[digits_num] = (10 - digits_num + 1) * dp[digits_num - 1]
        return sum(dp)

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total_sum = 10
        curr_dp = 9
        for digits_num in range(2, n + 1):
            curr_dp = (10 - digits_num + 1) * curr_dp
            total_sum += curr_dp
        return total_sum
