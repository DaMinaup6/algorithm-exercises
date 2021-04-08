# -----------------------------------------
# Model Solution
#
# Time  Complexity: O((n / b)^b * b)
# Space Complexity: O((n / b)^b)
# -----------------------------------------
# b := batchSize
# Ref:
# a) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1140548/Python-dfs-with-optimizations-explained
# b) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1141232/Python-DP-with-pruning
# c) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1141106/Math-proof-of-why-the-greedy-solution-works
# d) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1144399/Python-Top-Down-DP-with-a-little-greed
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        remain_groups = [group for group in groups if group % batchSize != 0]
        if len(remain_groups) == 0:
            return len(groups)
        happy_groups_count = len(groups) - len(remain_groups)

        # 1. Greedily serve all groups that are a multiple of batchSize first
        #   e.g. remain_groups == [1, 2, 3, 3, 5, 5, 5], batchSize == 4 => remainders_count == [0, 4, 1, 2]
        #        since remainder of 1 and 5 is 1, so put 4 for remainders_count[1], and so on
        remainders_count = [0] * batchSize
        for group in remain_groups:
            remainders_count[group % batchSize] += 1

        # 2. Greedily serve all pairs of groups where group_1 + group_2 is a multiple of batchsize
        #   group remainders to form a happy group
        #   e.g. batchSize == 4, remainders_count == [0, 4, 1, 2], we know that two groups with remainder 1 can group with other 2 groups with remainder 3 to form happy groups
        for remainder in range(1, batchSize // 2 + 1):
            if remainder * 2 == batchSize:
                happy_pairs = remainders_count[remainder] // 2
            else:
                happy_pairs = min(remainders_count[remainder], remainders_count[batchSize - remainder])
            remainders_count[remainder] -= happy_pairs
            remainders_count[batchSize - remainder] -= happy_pairs
            happy_groups_count += happy_pairs
        # can return happy_groups_count directly if all remainders used
        if all(remainder_count == 0 for remainder_count in remainders_count):
            return happy_groups_count

        # 3. Use top-down DP to find the optimal configuration of the remaining groups
        #   for the rest of the groups we use dp to store the result of each counter state
        #   we get a new group with fresh donuts only if that group has the same remainder as the sum of group sizes modulo batchSize
        @lru_cache(None)
        def dp(cnt):
            cnt = list(cnt)
            # remainders_sum_remainder := how many donuts left after giving donuts to remaining groups
            remainders_sum_remainder = sum(remainder * remainder_count for remainder, remainder_count in enumerate(cnt)) % batchSize

            extra_count = 0
            for remainder in range(1, batchSize):
                if cnt[remainder] == 0:
                    continue
                cnt[remainder] -= 1
                # if remainder == remainders_sum_remainder, which means the remaining groups is a multiple of batchSize, so current group must be a happy group
                extra_count = max(extra_count, dp(tuple(cnt)) + (1 if remainder == remainders_sum_remainder else 0))
                cnt[remainder] += 1
            return extra_count

        return happy_groups_count + dp(tuple(remainders_count))

# -----------------------------------------
# Bitmask Dynamic Programming
#
# Time  Complexity: O(n * 2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
# Ref:
# a) https://www.youtube.com/watch?v=ZpFno2IEHWE
# b) https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/
# Note: this solution will get a TLE result but it's an easier solution to understand
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        groups_size = len(groups)

        dp = [0] * (1 << groups_size)
        for mask in range(1 << groups_size):
            remain_donuts = 0
            for index in range(groups_size):
                if mask & (1 << index) != 0:
                    remain_donuts = (remain_donuts + groups[index]) % batchSize
            for index in range(groups_size):
                if mask & (1 << index) == 0:
                    # 以 batchSize == 3, groups == [1, 3] 為例
                    # 1. 舉例 mask == 2 (二進制為 10)，代表 groups[1] 已經被分派過甜甜圈
                    # 2. mask | (1 << index)，在 mask == 2, index == 0 的情形，mask | (1 << index) == 3（二進制為 11），代表在 groups[1] 已經被分派過甜甜圈的情形下考慮加入 groups[0] 時的 happy groups 數量
                    # 此時 remain_donuts == groups[1] % batchSize == 0
                    # mode_sum 的意義在於將 mask 中所有的 bit 1，也就是前面的組別都已經分配過甜甜圈之後，最後剩下的甜甜圈數量
                    # 若沒有剩下任何甜甜圈，也就是 mode_sum == 0，則要新增的組（在此為 groups[0]）必定為 happy group 因為這一組的人完全不會吃到剩餘的甜甜圈，因此 dp[mask | (1 << index)] 之一種可能性為 dp[mask] + 1
                    dp[mask | (1 << index)] = max(dp[mask | (1 << index)], dp[mask] + (1 if remain_donuts == 0 else 0))
        return dp[-1]
