# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(mn^3)
# Space Complexity: O(mn^2)
# -----------------------------------------
# m := len(key)
# NOTE: This solution causes TLE
from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_char_indexes = defaultdict(set)
        for index, char in enumerate(ring):
            ring_char_indexes[char].add(index)

        @lru_cache(None)
        def dfs(curr_ring_index, curr_key_index, curr_steps):
            if curr_key_index == len(key):
                return curr_steps

            curr_key_char = key[curr_key_index]
            if curr_ring_index in ring_char_indexes[curr_key_char]:
                return dfs(curr_ring_index, curr_key_index + 1, curr_steps + 1)

            min_steps = float('inf')
            for char_index in ring_char_indexes[curr_key_char]:
                smaller_index = min(char_index, curr_ring_index)
                greater_index = max(char_index, curr_ring_index)
                move_steps = min(greater_index - smaller_index, len(ring) + smaller_index - greater_index)
                if curr_steps + move_steps + 1 >= min_steps:
                    continue
                min_steps = min(min_steps, dfs(char_index, curr_key_index + 1, curr_steps + move_steps + 1))
            return min_steps

        return dfs(0, 0, 0)

# -----------------------------------------
# My Solution: DFS + Memoization (Enhanced)
#
# Time  Complexity: O(mn^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(key)
from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_char_indexes = defaultdict(set)
        for index, char in enumerate(ring):
            ring_char_indexes[char].add(index)

        @lru_cache(None)
        def min_steps_starts_from(ring_index, key_index):
            if key_index == len(key):
                return 0

            curr_key_char = key[key_index]
            if ring_index in ring_char_indexes[curr_key_char]:
                return 1 + min_steps_starts_from(ring_index, key_index + 1)

            min_steps = float('inf')
            for char_index in ring_char_indexes[curr_key_char]:
                move_steps = min(abs(char_index - ring_index), len(ring) - abs(char_index - ring_index))
                if move_steps + 1 >= min_steps:
                    continue
                min_steps = min(min_steps, move_steps + 1 + min_steps_starts_from(char_index, key_index + 1))
            return min_steps

        return min_steps_starts_from(0, 0)

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(mn^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(key)
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_char_indexes = defaultdict(set)
        for index, char in enumerate(ring):
            ring_char_indexes[char].add(index)

        min_steps = [[float('inf')] * (len(key) + 1) for _ in range(len(ring))]
        for ring_index in range(len(ring)):
            min_steps[ring_index][-1] = 0

        for key_index in range(len(key) - 1, -1, -1):
            for ring_index in range(len(ring) - 1, -1, -1):
                curr_key_char = key[key_index]
                if ring_index in ring_char_indexes[curr_key_char]:
                    min_steps[ring_index][key_index] = 1 + min_steps[ring_index][key_index + 1]
                    continue

                curr_min_steps = float('inf')
                for char_index in ring_char_indexes[curr_key_char]:
                    smaller_index = min(char_index, ring_index)
                    greater_index = max(char_index, ring_index)
                    move_steps = min(greater_index - smaller_index, len(ring) + smaller_index - greater_index)
                    if move_steps + 1 >= curr_min_steps:
                        continue
                    curr_min_steps = min(curr_min_steps, move_steps + 1 + min_steps[char_index][key_index + 1])
                min_steps[ring_index][key_index] = curr_min_steps
        return min_steps[0][0]

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(mn^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(key)
# Ref: https://www.pythonf.cn/read/161253
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_char_indexes = defaultdict(list)
        for index, char in enumerate(ring):
            ring_char_indexes[char].append(index)

        # min_steps[i][j] := min steps to match key from beginning to index i while ring index ends at j
        min_steps = [[float('inf')] * len(ring) for _ in range(len(key))]
        for index in ring_char_indexes[key[0]]:
            min_steps[0][index] = min(index, len(ring) - index) + 1

        for key_index in range(1, len(key)):
            for char_index in ring_char_indexes[key[key_index]]:
                for prev_char_index in ring_char_indexes[key[key_index - 1]]:
                    min_steps[key_index][char_index] = min(min_steps[key_index][char_index], min_steps[key_index - 1][prev_char_index] + min(abs(prev_char_index - char_index), len(ring) - abs(prev_char_index - char_index)) + 1)
        return min(min_steps[-1][char_index] for char_index in ring_char_indexes[key[-1]])

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(mn^2)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(key)
# Ref: http://bookshadow.com/weblog/2017/03/05/leetcode-freedom-trail/
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_char_indexes = defaultdict(list)
        for index, char in enumerate(ring):
            ring_char_indexes[char].append(index)

        prev_min_steps = [float('inf')] * len(ring)
        for index in ring_char_indexes[key[0]]:
            prev_min_steps[index] = min(index, len(ring) - index) + 1
        for key_index in range(1, len(key)):
            curr_min_steps = [float('inf')] * len(ring)
            for char_index in ring_char_indexes[key[key_index]]:
                for prev_char_index in ring_char_indexes[key[key_index - 1]]:
                    curr_min_steps[char_index] = min(curr_min_steps[char_index], prev_min_steps[prev_char_index] + min(abs(prev_char_index - char_index), len(ring) - abs(prev_char_index - char_index)) + 1)
            prev_min_steps = curr_min_steps

        return min(prev_min_steps[char_index] for char_index in ring_char_indexes[key[-1]])
