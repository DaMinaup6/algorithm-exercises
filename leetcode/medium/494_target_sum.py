# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := sum(nums), n := len(nums)

from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        val_diff = sum(nums) - S
        if val_diff < 0 or val_diff % 2 == 1:
            return 0
        elif val_diff == 0:
            return 2 ** nums.count(0)

        @lru_cache(None)
        def dfs(target, current_index, result):
            if target < 0:
                return result
            elif target == 0:
                return result + 1

            dfs_sum = 0
            for index in range(current_index, len(nums)):
                num = nums[index]
                if num == 0:
                    continue
                dfs_sum += dfs(target - 2 * num, index + 1, result)
            return result + dfs_sum

        return dfs(val_diff, 0, 0) * (2 ** nums.count(0))

# -----------------------------------------
# Dynamic Programming
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := sum(nums), n := len(nums)
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/80484450

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp[i][j] := how many ways to assign symbols to make sum of integers equal to j from start index to (i - 1)-th index of nums
        dp = [defaultdict(int) for _ in range(len(nums) + 1)] 
        dp[0][0] = 1
        for index, num in enumerate(nums):
            for current_sum, count in dp[index].items():
                dp[index + 1][current_sum + num] += count
                dp[index + 1][current_sum - num] += count

        return dp[len(nums)][S]
