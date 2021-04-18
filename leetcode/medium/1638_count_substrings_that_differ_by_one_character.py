# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^4)
# Space Complexity: O(n)
# -----------------------------------------
# n := min(len(s), len(t))
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if len(s) > len(t):
            s, t = t, s
        
        substrings_number = 0
        for window_size in range(1, len(s) + 1):
            for s_index in range(len(s) - window_size + 1):
                curr_s_substring = s[s_index:(s_index + window_size)]
                for t_index in range(len(t) - window_size + 1):
                    curr_t_substring = t[t_index:(t_index + window_size)]
                    if self.differ_by_one(curr_s_substring, curr_t_substring):
                        substrings_number += 1

        return substrings_number
    
    def differ_by_one(self, s_substring, t_substring):
        differ_count = 0
        for index in range(len(s_substring)):
            if s_substring[index] != t_substring[index]:
                differ_count += 1
            if differ_count > 1:
                return False

        return differ_count == 1

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(s), n := len(t)
# Ref: https://blog.csdn.net/qq_21201267/article/details/109433008
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        s_len, t_len, substrings_number = len(s), len(t), 0

        same = [[0] * t_len for _ in range(s_len)] # same[i][j] := how many substrings ends at s[i] and t[j] equal
        diff = [[0] * t_len for _ in range(s_len)] # diff[i][j] := how many substrings ends at s[i] and t[j] differ by "only one character"
        for index in range(s_len):
            same[index][0] = 1 if s[index] == t[0] else 0
            diff[index][0] = 0 if s[index] == t[0] else 1
        for index in range(t_len):
            same[0][index] = 1 if s[0] == t[index] else 0
            diff[0][index] = 0 if s[0] == t[index] else 1

        for s_index in range(1, s_len):
            for t_index in range(1, t_len):
                if s[s_index] == t[t_index]:
                    same[s_index][t_index] = same[s_index - 1][t_index - 1] + 1
                    diff[s_index][t_index] = diff[s_index - 1][t_index - 1]
                else:
                    diff[s_index][t_index] = same[s_index - 1][t_index - 1] + 1

        for s_index in range(s_len):
            for t_index in range(t_len):
                substrings_number += diff[s_index][t_index]
        return substrings_number
