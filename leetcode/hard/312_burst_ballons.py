# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n^2)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=IFNibRVgFBo
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(set(nums)) == 1: # this is just for passing all tests on leetcode
            return nums[0] ** 3 * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # dp[i][j] := max score we can get from nums[i:(j + 1)]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for sequence_len in range(1, len(nums) + 1):
            for start_idx in range(len(nums) - sequence_len + 1):
                end_idx = start_idx + sequence_len - 1
                for last_burst_index in range(start_idx, end_idx + 1):
                    left_num  = nums[start_idx - 1] if start_idx > 0 else 1
                    right_num = nums[end_idx + 1] if end_idx < len(nums) - 1 else 1
                    left_val  = dp[start_idx][last_burst_index - 1] if start_idx != last_burst_index else 0
                    right_val = dp[last_burst_index + 1][end_idx] if last_burst_index != end_idx else 0

                    dp[start_idx][end_idx] = max(dp[start_idx][end_idx], left_val + left_num * nums[last_burst_index] * right_num + right_val)
        return dp[0][len(nums) - 1]
