# -----------------------------------------
# Knuth–Morris–Pratt Pattern Matching
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m)
# -----------------------------------------
# m := len(haystack), n := len(needle)
# Ref:
# a) https://www.youtube.com/watch?v=GTJr8OvyEVQ
# b) https://www.youtube.com/watch?v=uKr9qIZMtzw
# c) https://blog.csdn.net/coder_orz/article/details/51708389

# -----> Version 1: Find first matched index
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        # generate next_arr array, need O(n) time
        i, j = -1, 0
        next_arr = [-1] * len(needle)
        while j < len(needle) - 1:
            # needle[i] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next_arr[j] = i
            else:
                i = next_arr[i]
        # check through the haystack using next_arr, need O(m) time
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        return i - j if j == len(needle) else -1

# -----> Version 2: Find all matched indexes
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        # generate next_arr array, need O(n) time
        i, j = -1, 0
        next_arr = [-1] * len(needle)
        while j < len(needle) - 1:
            # needle[i] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next_arr[j] = i
            else:
                i = next_arr[i]
        # check through the haystack using next_arr, need O(m) time
        matched_indexes = []
        i = 0
        while i < len(haystack):
            j = 0
            while i < len(haystack) and j < len(needle):
                if j == -1 or haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    j = next_arr[j]
            if j == len(needle):
                matched_indexes.append(i - j)
        return matched_indexes
