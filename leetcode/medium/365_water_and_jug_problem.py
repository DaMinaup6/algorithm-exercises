# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(mn))
# Space Complexity: O(1)
# -----------------------------------------
# m := jug1Capacity, n := jug2Capacity
# Ref: https://stackoverflow.com/a/22112305
import math

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0
