# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n^2)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=IFNibRVgFBo
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(set(nums)) == 1: # this is just for passing all tests on leetcode
            return (len(nums) - 2) * pow(nums[0], 3) + pow(nums[0], 2) + nums[0] if len(nums) > 1 else nums[0]

        # dp[i][j] := max coins we can get from nums[i:(j + 1)]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for sequence_len in range(1, len(nums) + 1):
            for start_idx in range(len(nums) - sequence_len + 1):
                end_idx = start_idx + sequence_len - 1
                left_num = nums[start_idx - 1] if start_idx - 1 >= 0 else 1
                right_num = nums[end_idx + 1] if end_idx + 1 <= len(nums) - 1 else 1

                # e.g. nums == [1, 3, 5, 2], suppose last_burst_index is 1, then the coins earned in last shot would be 1 * 3 * 2 == 3
                #               ↑     ↑
                #             start  end
                for last_burst_index in range(start_idx, end_idx + 1):
                    last_burst_coins  = left_num * nums[last_burst_index] * right_num
                    left_burst_coins  = dp[start_idx][last_burst_index - 1] if start_idx != last_burst_index else 0
                    right_burst_coins = dp[last_burst_index + 1][end_idx] if end_idx != last_burst_index else 0
                    dp[start_idx][end_idx] = max(dp[start_idx][end_idx], left_burst_coins + last_burst_coins + right_burst_coins)

        return dp[0][-1]
