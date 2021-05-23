# -----------------------------------------
# Model Solution: BFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(s)
# Ref: https://www.youtube.com/watch?v=v1HpZUnQ4Yo
from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        queue, farthest = deque([0]), 0
        while len(queue) > 0:
            index = queue.popleft()
            start = max(index + minJump, farthest + 1)
            for next_index in range(start, min(index + maxJump + 1, len(s))):
                if s[next_index] == "0":
                    queue.append(next_index)
                    if next_index == len(s) - 1:
                        return True
            farthest = index + maxJump
        return False

# -----------------------------------------
# Model Solution: Greedy
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(s)
# Ref: https://leetcode.com/problems/jump-game-vii/discuss/1224969/Python3-Greedy-O(n)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        min_i = max_i = 0
        for index in range(len(s) - 1):
            if s[index] == '1' or index < min_i:
                continue
            if index > max_i:
                return False

            min_i = index + minJump
            max_i = min(index + maxJump, len(s) - 1)
            if min_i <= len(s) - 1 <= max_i:
                return True
        return False
