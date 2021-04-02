# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n + mw) == O(mw)
# Space Complexity: O(n)      == O(1)
# -----------------------------------------
# m := len(words), n := len(order) == 26, w := max([len(word) for word in words])
# Ref: https://leetcode.com/problems/verifying-an-alien-dictionary/solution/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order_map = {}
        for index, val in enumerate(order):
            char_order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if char_order_map[words[i][j]] > char_order_map[words[i + 1][j]]:
                        return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True
