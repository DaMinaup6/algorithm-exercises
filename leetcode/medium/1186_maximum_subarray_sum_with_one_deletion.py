# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(n)
# -----------------------------------------

# -----> Version 1: Space Complexity: O(n)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp[i][0] := max sum of subarray ends at index i with 0 deletion
        # dp[i][1] := max sum of subarray ends at index i with 1 deletion
        dp = [[0, 0] for _ in arr]
        dp[0] = [arr[0], 0]

        max_sum = arr[0]
        for index in range(1, len(arr)):
            # add curr num to previous subarray or starts with a new subarray
            dp[index][0] = max(arr[index] + dp[index - 1][0], arr[index])
            # delete curr num or add curr num to previous subarray with one deletion
            dp[index][1] = max(dp[index - 1][0], dp[index - 1][1] + arr[index])
            max_sum = max(max_sum, dp[index][0], dp[index][1])
        return max_sum

# -----> Version 2: Space Complexity: O(1)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        curr_dp = [arr[0], 0]
        max_sum = arr[0]
        for index in range(1, len(arr)):
            curr_dp[0], curr_dp[1] = max(arr[index] + curr_dp[0], arr[index]), max(curr_dp[0], curr_dp[1] + arr[index])
            max_sum = max(max_sum, curr_dp[0], curr_dp[1])
        return max_sum
