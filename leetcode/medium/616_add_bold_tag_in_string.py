# -----------------------------------------
# My Solution
#
# Time  Complexity: O(d(m + n) + nlog(n) + n)
# Space Complexity: O(n)
# -----------------------------------------
# d := len(dict), m := max(len(word) for word in dict), n := len(string)
# Note: This solution requires KMP pattern matching algorithm
from collections import deque

def kmp_matched_indexes(haystack, needle):
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
            matched_indexes.append((i - j, i - j + len(needle) - 1))

    return matched_indexes

def add_bold_tag(string, dict):
    if len(dict) == 0:
        return string

    matched_intervals = []
    for word in dict:
        for interval in kmp_matched_indexes(string, word):
            matched_intervals.append(interval)
    if len(matched_intervals) == 0:
        return string

    matched_intervals = deque(sorted(matched_intervals))
    interval_pointer  = 0
    while interval_pointer < len(matched_intervals) - 1:
        curr_interval, next_interval = matched_intervals[interval_pointer], matched_intervals[interval_pointer + 1]
        if curr_interval[0] <= next_interval[0] <= curr_interval[1] + 1:
            matched_intervals[interval_pointer + 1] = (curr_interval[0], max(curr_interval[1], next_interval[1]))
            matched_intervals.popleft()
        else:
            interval_pointer += 1

    bold_tags_string = ""
    interval_pointer = 0
    for string_index in range(len(string)):
        curr_interval = matched_intervals[interval_pointer] if interval_pointer < len(matched_intervals) else None
        if curr_interval is None or string_index not in curr_interval:
            bold_tags_string += string[string_index]
        elif string_index == curr_interval[0]:
            bold_tags_string += "<b>" + string[string_index]
        elif string_index == curr_interval[1]:
            bold_tags_string += string[string_index] + "</b>"
            interval_pointer += 1
    return bold_tags_string

print(add_bold_tag("abcxyz123", ["abc","123"]) == "<b>abc</b>xyz<b>123</b>")
print(add_bold_tag("aaabbcc", ["aaa", "aab", "bc"]) == "<b>aaabbc</b>c")
