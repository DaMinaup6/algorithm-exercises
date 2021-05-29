# -----------------------------------------
# Model Solution: DFS + Bitmask
#
# Time  Complexity: O(n^2 * 2^n)
# Space Complexity: O(n * 2^n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/discuss/1238657/Python3.-Straightforward-dp-with-using-bit-mask
from functools import lru_cache

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def cal_min_xor_sum(index_1, bitmask):
            if index_1 == len(nums1):
                return 0

            min_xor_sum = float('inf')
            for index_2 in range(len(nums2)):
                # if bitmask & (1 << index_2) == 0, which means nums2[index_2] not used yet
                if bitmask & (1 << index_2) == 0:
                    curr_xor_sum = (nums1[index_1] ^ nums2[index_2]) + cal_min_xor_sum(index_1 + 1, bitmask | (1 << index_2))
                    min_xor_sum  = min(min_xor_sum, curr_xor_sum)
            return min_xor_sum

        return cal_min_xor_sum(0, 0)
