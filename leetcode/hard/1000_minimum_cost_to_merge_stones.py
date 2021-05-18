# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^3 / k)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(stones)
# Ref: https://www.youtube.com/watch?v=FabkoUzs64o
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - 1) % (k - 1) != 0:
            return -1

        pre_sums = [0]
        for stone in stones:
            pre_sums.append(pre_sums[-1] + stone)

        # dp[i][j] := min cost to merge subarray stones[i:(j + 1)] into (j - i) % (k - 1) + 1 piles
        dp = [[float('inf')] * len(stones) for _ in stones]
        for index in range(len(stones)):
            dp[index][index] = 0

        for sub_arr_len in range(2, len(stones) + 1):
            for start_index in range(len(stones) - sub_arr_len + 1):
                end_index = start_index + sub_arr_len - 1
                for split_index in range(start_index, end_index, k - 1):
                    dp[start_index][end_index] = min(dp[start_index][end_index], dp[start_index][split_index] + dp[split_index + 1][end_index])
                if (sub_arr_len - 1) % (k - 1) == 0:
                    dp[start_index][end_index] += pre_sums[end_index + 1] - pre_sums[start_index]
        return dp[0][-1]
