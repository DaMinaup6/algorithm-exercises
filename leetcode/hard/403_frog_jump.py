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

        positions = set(stones)
        last_position = max(stones)

        @lru_cache(None)
        def can_cross_from(curr_position, last_jump):
            if curr_position == last_position:
                return True

            for next_jump in (last_jump - 1, last_jump, last_jump + 1):
                if next_jump > 0 and curr_position + next_jump in positions and can_cross_from(curr_position + next_jump, next_jump):
                    return True
            return False

        return can_cross_from(1, 1)

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

        stones_position_index_map = {}
        for index, stone_position in enumerate(stones):
            stones_position_index_map[stone_position] = index

        prev_jump_units = [set() for _ in stones]
        prev_jump_units[0] = set([0])
        for index in range(len(stones)):
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
