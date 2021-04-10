# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(2^q)
# Space Complexity: O(q)
# -----------------------------------------
# q := number of question marks
# Ref: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145#analysis
import sys
from functools import lru_cache

def calc_min_cost(x, y, string):
    @lru_cache(None)
    def dp(chars):
        if len(chars) <= 1:
            return 0
        chars = list(chars)
        if chars[0] == '?':
            return min(
                dp(tuple(['C'] + chars[1:])),
                dp(tuple(['J'] + chars[1:])),
            )
        if chars[0] != '?' and chars[1] == '?':
            return min(
                dp(tuple([chars[0], 'C'] + chars[2:])),
                dp(tuple([chars[0], 'J'] + chars[2:])),
            )
        if chars[0] == 'C' and chars[1] == 'J':
            return x + dp(tuple(chars[1:]))
        if chars[0] == 'J' and chars[1] == 'C':
            return y + dp(tuple(chars[1:]))
        while len(chars) >= 2 and chars[0] == chars[1]:
            chars.pop(0)
        return dp(tuple(chars))
    return dp(tuple([char for char in string]))

sys.setrecursionlimit(2 ** 31 - 1)

t = int(input())
for i in range(1, t + 1):
    x, y, string = input().split(" ")
    print("Case #{}: {}".format(i, calc_min_cost(int(x), int(y), string)))
