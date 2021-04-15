# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ord_dict = defaultdict(int) # if input contains unicode characters then we should use hash
        t_ord_dict = defaultdict(int)
        for index in range(len(s)):
            s_ord_dict[s[index]] += 1
            t_ord_dict[t[index]] += 1

        return s_ord_dict == t_ord_dict
