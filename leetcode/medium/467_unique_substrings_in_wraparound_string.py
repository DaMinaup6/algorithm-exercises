# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(26)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/83088406
import collections

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        max_length_ends_with = collections.defaultdict(int)

        # e.g. p == "bcabc"
        #      the substring "bc" is duplicated in substring "abc", need to avoid calculating twice
        #      so we check the max length ends with some character to help us
        #      for this p, we will get max_length_ends_with == {"a": 1, "b": 2, "c": 3}
        #      so first "bc" is contained in second substring
        consecutive = 0
        for index in range(len(p)):
            if index > 0 and (ord(p[index]) - ord(p[index - 1]) == 1 or p[index] == 'a' and p[index - 1] == 'z'):
                consecutive += 1
            else:
                consecutive = 1
            max_length_ends_with[p[index]] = max(max_length_ends_with[p[index]], consecutive)
        return sum(max_length_ends_with.values())
