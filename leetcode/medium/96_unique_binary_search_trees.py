# -----------------------------------------
# My Solution: normal cache
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Note: thid method would raise RecursionError: maximum recursion depth exceeded in comparison if n is large
class Solution:
    def numTrees(self, n: int) -> int:
        cache = { 1: 1 }

        def num_tree_recursion(num):
            if num == 0 or num == 1:
                return 1
            if cache.get(num) is not None:
                return cache[num]

            trees_num = 0
            for left_subtree_size in range(0, num):
                trees_num += num_tree_recursion(left_subtree_size) * num_tree_recursion(num - 1 - left_subtree_size)
            cache[num] = trees_num

            return trees_num

        return num_tree_recursion(n)

# -----------------------------------------
# My Solution: use LRU cache from functools
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Note: thid method would raise RecursionError: maximum recursion depth exceeded in comparison if n is large
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        trees_num = 0
        for left_subtree_size in range(0, n):
            trees_num += self.numTrees(left_subtree_size) * self.numTrees(n - 1 - left_subtree_size)

        return trees_num

# -----------------------------------------
# Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]
