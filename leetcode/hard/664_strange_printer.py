# -----------------------------------------
# Model Solution: DFS + Memoization
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n^2)
# -----------------------------------------
# m := len(s)
# Ref:
# a) https://leetcode.com/problems/strange-printer/discuss/1205305/Python3-180ms-beating-100
# b) https://www.cnblogs.com/grandyang/p/8319913.html
from collections import defaultdict
from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        char_indexes = defaultdict(list)
        for index, char in enumerate(s):
            char_indexes[char].append(index)

        @lru_cache(None)
        def min_turns_between(start_index, end_index):
            if start_index == end_index:
                return 1

            # heuristic:
            # a) if only one unique char -> only one turn needed
            # b) if all chars different  -> need (end_index - start_index + 1) turns
            curr_string = s[start_index:(end_index + 1)]
            uniq_chars  = len(set(curr_string))
            if uniq_chars == 1:
                return 1
            if uniq_chars == len(curr_string):
                return len(curr_string)

            # initialize min_turns by considerring printer only print first char and then print the remaining chars
            min_turns = 1 + min_turns_between(start_index + 1, end_index)
            for next_char_index in char_indexes[s[start_index]]:
                if start_index < next_char_index <= end_index:
                    # e.g. s == "abbac", self.strangePrinter("abbac") == self.strangePrinter("bb") + self.strangePrinter("ac")
                    min_turns = min(min_turns, min_turns_between(start_index + 1, next_char_index - 1) + min_turns_between(next_char_index, end_index))
            return min_turns

        return min_turns_between(0, len(s) - 1)
