# -----------------------------------------
# Model Solution: Recursion + Memoization
#
# Time  Complexity: O(2^m)
# Space Complexity: O(2^m)
# -----------------------------------------
# m := maxChoosableInteger
# Ref: https://www.youtube.com/watch?v=GNZIAbf0gT0
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        all_nums_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if all_nums_sum < desiredTotal:
            return False
        if all_nums_sum == desiredTotal:
            return maxChoosableInteger % 2 == 1

        def win(curr_sum, memories, state):
            if curr_sum >= desiredTotal: # previous player already made curr_sum >= desiredTotal, so current player loses
                return False
            if memories[state] != 0:
                return memories[state] == 1
            for num_index in range(maxChoosableInteger):
                if (state & (1 << num_index)) > 0:
                    continue
                if not win(curr_sum + num_index + 1, memories, state | (1 << num_index)):
                    memories[state] = 1
                    return True
            memories[state] = -1
            return False

        memories = [0] * (1 << maxChoosableInteger)
        return win(0, memories, 0)

# -----------------------------------------
# Model Solution: Recursion + Memoization
#
# Time  Complexity: O(2^m)
# Space Complexity: O(2^m)
# -----------------------------------------
# Ref: https://leetcode.com/problems/can-i-win/discuss/1023093/python-short-solution
from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def can_win(curr_sum, used_nums):
            for num in range(1, maxChoosableInteger + 1):
                bit_index = num - 1
                if used_nums & (1 << bit_index) == 0:
                    # if current user acheives the desired number or next user have a chance to lose, current user wins
                    if curr_sum + num >= desiredTotal or not can_win(curr_sum + num, used_nums | (1 << bit_index)):
                        return True
            return False

        return can_win(0, 0)
