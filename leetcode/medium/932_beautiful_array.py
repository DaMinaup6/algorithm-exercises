# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(nlog(n))
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/beautiful-array/solution/
# b) https://www.cnblogs.com/grandyang/p/12287146.html
from functools import lru_cache

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        @lru_cache(None)
        def beautiful_array(n):
            if n == 1:
                return [1]
            odds  = beautiful_array((n + 1) // 2)
            evens = beautiful_array(n // 2)
            return [2 * num - 1 for num in odds] + [2 * num for num in evens]

        return beautiful_array(N)
