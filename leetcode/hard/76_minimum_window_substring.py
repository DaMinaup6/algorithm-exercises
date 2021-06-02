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

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(s), n := len(t)
# Ref: https://blog.csdn.net/XX_123_1_RJ/article/details/86756306
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars_count = collections.Counter(t)
        miss_char_num = len(t)

        left_pointer = sub_str_left = sub_str_right = 0
        for right_pointer, char in enumerate(s):
            if char in t_chars_count:
                if t_chars_count[char] > 0:
                    miss_char_num -= 1
                t_chars_count[char] -= 1

            # e.g. s == "DAABC", t == "ABC"
            #      when right_pointer reaches index 4, we have t_chars_count == { "A": -1, "B": 0, "C": 0 }
            #      since "D" not in t so it can be skipped, obviously
            #      and t_chars_count["A"] < 0, which means that we have contained more "A" than needed in t, so the first "A" can be skipped, too
            if miss_char_num == 0:
                # if s[left_pointer] not in t_chars_count then it means it can be skipped
                while left_pointer < right_pointer and (s[left_pointer] not in t_chars_count or t_chars_count[s[left_pointer]] < 0):
                    if s[left_pointer] in t_chars_count:
                        t_chars_count[s[left_pointer]] += 1
                    left_pointer += 1
                if sub_str_right == 0 or (right_pointer + 1) - left_pointer <= sub_str_right - sub_str_left:
                    sub_str_left, sub_str_right = left_pointer, (right_pointer + 1)
        return s[sub_str_left:sub_str_right]
