# -----------------------------------------
# Model Solution
#
# Time  Complexity: O((n / K)^K * K)
# Space Complexity: O((n / K)^K * K)
# -----------------------------------------
# K := batchSize // 2
# Ref:
# a) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1140548/Python-dfs-with-optimizations-explained
# b) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1141232/Python-DP-with-pruning
# c) https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1141106/Math-proof-of-why-the-greedy-solution-works
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        remain_groups = [group for group in groups if group % batchSize != 0]
        if len(remain_groups) == 0:
            return len(groups)
        happy_groups_count = len(groups) - len(remain_groups)

        # e.g. remain_groups == [1, 2, 3, 3, 5, 5, 5], batchSize == 4 => remainders_count == [0, 4, 1, 2]
        #      since remainder of 1 and 5 is 1, so put 4 for remainders_count[1], and so on
        remainders_count = [0] * batchSize
        for group in remain_groups:
            remainders_count[group % batchSize] += 1

        # group remainders to form a happy group
        # e.g. batchSize == 4, remainders_count == [0, 4, 1, 2], we know that two groups with remainder 1 can group with other 2 groups with remainder 3 to form happy groups
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

        # for the rest of the groups we use dp to store the result of each counter state
        # we get a new group with fresh donuts only if that group has the same remainder as the sum of group sizes modulo batchSize
        @lru_cache(None)
        def dp(cnt):
            cnt = list(cnt)
            remainders_sum_remainder = sum(remainder * remainder_count for remainder, remainder_count in enumerate(cnt)) % batchSize

            extra_count = 0
            for remainder in range(1, batchSize):
                if cnt[remainder] == 0:
                    continue
                cnt[remainder] -= 1
                extra_count = max(extra_count, dp(tuple(cnt)) + (1 if remainder == remainders_sum_remainder else 0))
                cnt[remainder] += 1
            return extra_count

        return happy_groups_count + dp(tuple(remainders_count))
