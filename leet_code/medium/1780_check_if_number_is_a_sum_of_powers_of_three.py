# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(log(n))
# -----------------------------------------
import math

class Solution:
    def checkPowersOfThree(self, n):
        used_powers = dict()

        while n > 0:
            power = math.floor(math.log(n, 3))

            if used_powers.get(power) is None:
                used_powers[power] = True
                n -= 3 ** power
            else:
                return False

        return n == 0
