# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(s), n := len(t)
# from collections import defaultdict
#
# def window_valid(s_count, t_count):
#     for char in t_count:
#         if t_count[char] > s_count[char]:
#             return False
#
#     return True
#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_count = defaultdict(int)
#         for char in t:
#             t_count[char] += 1
#
#         s_count = defaultdict(int)
#         s_count[s[0]] = 1
#         left_cursor   = 0
#         right_cursor  = 0
#         sub_s_indexes = [-1, -1]
#         while left_cursor <= right_cursor and right_cursor < len(s):
#             if window_valid(s_count, t_count):
#                 if sub_s_indexes == [-1, -1] or sub_s_indexes[1] - sub_s_indexes[0] + 1 > right_cursor - left_cursor + 1:
#                     sub_s_indexes = [left_cursor, right_cursor]
#
#                 s_count[s[left_cursor]] -= 1
#                 left_cursor += 1
#             else:
#                 right_cursor += 1
#                 if right_cursor < len(s):
#                     s_count[s[right_cursor]] += 1
#
#         return s[sub_s_indexes[0]:(sub_s_indexes[1] + 1)]

# -----------------------------------------
# My Solution (enhanced)
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(s), n := len(t)
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        uniq_char_num = len(t_count)

        s_count = defaultdict(int)
        s_count[s[0]] = 1
        char_full_num = 1 if s[0] in t_count and 1 >= t_count[s[0]] else 0

        left_cursor   = 0
        right_cursor  = 0
        sub_s_indexes = [-1, -1]
        while left_cursor <= right_cursor and right_cursor < len(s):
            if char_full_num == uniq_char_num:
                if sub_s_indexes == [-1, -1] or sub_s_indexes[1] - sub_s_indexes[0] + 1 > right_cursor - left_cursor + 1:
                    sub_s_indexes = [left_cursor, right_cursor]

                s_count[s[left_cursor]] -= 1
                if s[left_cursor] in t_count and s_count[s[left_cursor]] < t_count[s[left_cursor]]:
                    char_full_num -= 1
                left_cursor += 1
            else:
                right_cursor += 1
                if right_cursor < len(s):
                    s_count[s[right_cursor]] += 1
                    # must use == instead of >=, for example
                    # s == "ABBC", t == 'ABC', if use >= then "ABB" will considered as valid window since when "B" of "AB" and last "B" of "ABB" matches >= condition
                    if s[right_cursor] in t_count and s_count[s[right_cursor]] == t_count[s[right_cursor]]:
                        char_full_num += 1

        return s[sub_s_indexes[0]:(sub_s_indexes[1] + 1)]
