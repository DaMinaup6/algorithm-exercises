# -----------------------------------------
# My Solution: DFS + Memoization
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] > 1:
            return False
        if len(stones) == 2:
            return True

        stones_position_index_map = {}
        for index, stone_position in enumerate(stones):
            stones_position_index_map[stone_position] = index

        @lru_cache(None)
        def dfs(curr_stone_index, prev_jump_unit):
            if curr_stone_index == len(stones) - 1:
                return True

            curr_position = stones[curr_stone_index]
            for next_jump_unit in [prev_jump_unit - 1, prev_jump_unit, prev_jump_unit + 1]:
                if next_jump_unit <= 0 or curr_position + next_jump_unit not in stones_position_index_map:
                    continue
                next_stone_index = stones_position_index_map[curr_position + next_jump_unit]
                if dfs(next_stone_index, next_jump_unit):
                    return True
            return False

        return dfs(1, 1)

# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] > 1:
            return False
        if len(stones) == 2:
            return True

        stones_position_index_map = {}
        for index, stone_position in enumerate(stones):
            stones_position_index_map[stone_position] = index

        prev_jump_units = [set() for _ in stones]
        prev_jump_units[0], prev_jump_units[1] = set([0]), set([1])
        for index in range(1, len(stones)):
            curr_position = stones[index]
            for prev_jump_unit in prev_jump_units[index]:
                for next_jump_unit in [prev_jump_unit - 1, prev_jump_unit, prev_jump_unit + 1]:
                    if next_jump_unit > 0 and curr_position + next_jump_unit in stones_position_index_map:
                        next_index = stones_position_index_map[curr_position + next_jump_unit]
                        if next_index == len(stones) - 1:
                            return True
                        else:
                            prev_jump_units[next_index].add(next_jump_unit)
        return False
