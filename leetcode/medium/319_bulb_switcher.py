# -----------------------------------------
# My Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # only square indexes (1-base) remains turned on. e.g. 1, 4, 9, 16, ...
        if n == 0:
            return 0

        return int(math.sqrt(n))
