# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(tops) == len(bottoms)
from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domino_size = len(tops)

        top_nums_indexes = defaultdict(set)
        bot_nums_indexes = defaultdict(set)
        all_nums_indexes = defaultdict(set)
        for index in range(domino_size):
            top_num, bot_num = tops[index], bottoms[index]
            top_nums_indexes[top_num].add(index)
            bot_nums_indexes[bot_num].add(index)
            all_nums_indexes[top_num].add(index)
            all_nums_indexes[bot_num].add(index)

        min_swaps = float('inf')
        for curr_nums_indexes, other_nums_indexes in ((top_nums_indexes, bot_nums_indexes), (bot_nums_indexes, top_nums_indexes)):
            for num in curr_nums_indexes:
                if len(all_nums_indexes[num]) != domino_size:
                    continue
                nums_indexes = curr_nums_indexes[num]
                miss_indexes = set(range(domino_size)) - nums_indexes
                all_miss_found = (len(miss_indexes) == 0) or all(miss_index in other_nums_indexes[num] for miss_index in miss_indexes)
                if all_miss_found:
                    min_swaps = min(min_swaps, len(miss_indexes))
        return min_swaps if min_swaps != float('inf') else -1

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(tops) == len(bottoms)
# Ref: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC%2B%2BPython-Different-Ideas
from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domino_size = len(tops)

        top_nums_counter = defaultdict(int)
        bot_nums_counter = defaultdict(int)
        same_num_counter = defaultdict(int)
        for index in range(domino_size):
            top_num, bot_num = tops[index], bottoms[index]
            top_nums_counter[top_num] += 1
            bot_nums_counter[bot_num] += 1
            if top_num == bot_num:
                same_num_counter[top_num] += 1

        min_swaps = float('inf')
        for num in range(1, 7):
            if top_nums_counter[num] + bot_nums_counter[num] - same_num_counter[num] == domino_size:
                min_swaps = min(min_swaps, domino_size - max(top_nums_counter[num], bot_nums_counter[num]))
        return min_swaps if min_swaps != float('inf') else -1
