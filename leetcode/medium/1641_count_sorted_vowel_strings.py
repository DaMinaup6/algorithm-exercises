# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def countVowelStrings(self, n: int) -> int:
        aeiou_nums = [1] * 5
        for layer in range(2, n + 1):
            # e.g. n == 3
            # we have 15 strings previously
            # aa             (1 strings ends with "a")
            # ae ee          (2 strings ends with "e")
            # ai ei ii       (3 strings ends with "i")
            # ao eo io oo    (4 strings ends with "o")
            # au eu iu ou uu (5 strings ends with "u")
            # you can see there is one string for us to put "a" behind, which is "aa"
            # and there are (1 + 2) == 3 strings for us to put "e" behind, which are "aa", "ae" and "ee"
            # and there are (1 + 2 + 3) == 6 strings for us to put "i" behind, which are...
            # at the end we would have 1 string ends with "a", 3 strings ends with "e", ... => aeiou_nums == [1, 3, 6, 10, 15]
            # so ans for n == 3 is sum(aeiou_nums) == 35
            for index in range(1, 5):
                aeiou_nums[index] += aeiou_nums[index - 1]
        return sum(aeiou_nums)
