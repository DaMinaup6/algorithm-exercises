# -----------------------------------------
# Model Solution: BFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=s66-UqMDoAo
from collections import deque

class Solution:
    def minDays(self, n: int) -> int:
        checked_orange_nums = {n}
        queue = deque([n])
        days  = 0
        while len(queue) > 0:
            current_size = len(queue)
            while current_size > 0:
                left_oranges = queue.popleft()

                if left_oranges == 0:
                    return days
                if left_oranges % 3 == 0 and (left_oranges // 3) not in checked_orange_nums:
                    queue.append(left_oranges // 3)
                    checked_orange_nums.add(left_oranges // 3)
                if left_oranges % 2 == 0 and (left_oranges // 2) not in checked_orange_nums:
                    queue.append(left_oranges // 2)
                    checked_orange_nums.add(left_oranges // 2)
                if left_oranges - 1 not in checked_orange_nums:
                    queue.append(left_oranges - 1)
                    checked_orange_nums.add(left_oranges - 1)
                current_size -= 1

            days += 1

        return -1

# -----------------------------------------
# Model Solution: Dynamic Programming + Greddy
#
# Time  Complexity: O((log(n))^2)
# Space Complexity: O((log(n))^2)
# -----------------------------------------
# Ref:
# a) https://www.youtube.com/watch?v=s66-UqMDoAo
# b) https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/discuss/794847/Polylogarithmic-solution
from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dfs(left_oranges):
            if left_oranges <= 1:
                return left_oranges
            return 1 + min(left_oranges % 2 + dfs(left_oranges // 2), left_oranges % 3 + dfs(left_oranges // 3))
        return dfs(n)
