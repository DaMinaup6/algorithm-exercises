# -----------------------------------------
# My Solution
#
# Time  Complexity: O(r * (mlog(m) + log(n)) + mlog(m) + m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(p), n := len(s), r := len(removable)
from collections import defaultdict
import bisect

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        s_char_indexes = defaultdict(list)
        for index, char in enumerate(s):
            s_char_indexes[char].append(index)
        p_chars_set = set(p)

        curr_subsequence = []
        prev_char_index  = -1
        for char in p:
            position = bisect.bisect_left(s_char_indexes[char], prev_char_index + 1)
            prev_char_index = s_char_indexes[char][position]
            curr_subsequence.append(prev_char_index)

        def update_curr_subsequence_from(start_position):
            for curr_position in range(start_position, len(curr_subsequence)):
                if curr_position != start_position and curr_subsequence[curr_position] > curr_subsequence[curr_position - 1]:
                    break
                curr_s_index  = curr_subsequence[curr_position]
                curr_s_char   = s[curr_s_index]
                next_s_index  = 1 + max(curr_s_index, curr_subsequence[curr_position - 1] if curr_position > 0 else curr_s_index)
                next_position = bisect.bisect_left(s_char_indexes[curr_s_char], next_s_index)
                if next_position == len(s_char_indexes[curr_s_char]):
                    return False
                curr_subsequence[curr_position] = s_char_indexes[curr_s_char][next_position]
            return True

        removals = 0
        for removable_index in removable:
            s_char = s[removable_index]
            remove_position = bisect.bisect_left(s_char_indexes[s_char], removable_index)
            del s_char_indexes[s_char][remove_position]

            if s_char in p_chars_set:
                position = bisect.bisect_left(curr_subsequence, removable_index)
                if position < len(curr_subsequence) and curr_subsequence[position] == removable_index and not update_curr_subsequence_from(position):
                    break
            removals += 1
        return removals

# -----------------------------------------
# Model Solution: Binary Search
#
# Time  Complexity: O((m + n + r) * log(r))
# Space Complexity: O(r)
# -----------------------------------------
# m := len(p), n := len(s), r := len(removable)
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check_subsequence_valid(removable_index):
            removed_indexes_set  = set(removable[:(removable_index + 1)])
            s_pointer, p_pointer = 0, 0
            while s_pointer < len(s) and p_pointer < len(p):
                if s_pointer in removed_indexes_set:
                    s_pointer += 1
                elif s[s_pointer] == p[p_pointer]:
                    s_pointer += 1
                    p_pointer += 1
                else:
                    s_pointer += 1
            return p_pointer == len(p)

        left_pointer, right_pointer = 0, len(removable) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if check_subsequence_valid(middle_pointer):
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        return right_pointer + 1
