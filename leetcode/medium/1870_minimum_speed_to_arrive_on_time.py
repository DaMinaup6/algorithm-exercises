# -----------------------------------------
# My Solution: Binary Search
#
# Time  Complexity: O(nlog(m))
# Space Complexity: O(1)
# -----------------------------------------
# m := max(dist), n := len(dist)
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # min total_hour would be (len(dist) - 1 + dist[-1] / speed), which is greater than (len(dist) - 1)
        # if total_hour == len(dist) - 1 + dist[-1] / speed, then the speed must be max(dist) or math.ceil(dist[-1] / round(hour % 1, 2))
        # e.g. dist == [1, 1, 100000], hour == 2.01
        # we need dist[-1] / speed <= 0.01 to satisfy that total_hour <= hour, so speed >= dist[-1] / 0.01
        # but for dist == [1, 100, 1], hour == 2.2, dist[-1] / 0.2 == 5, then total_hour would be 21.2, so need consider max(dist) also
        if len(dist) - 1 >= math.ceil(hour):
            return -1
        if hour % 1 != 0 and len(dist) - 1 == math.floor(hour):
            return max(max(dist), math.ceil(dist[-1] / round(hour % 1, 2)))

        # this would be an array in decreasing order, find the min speed such that total_hour <= hour
        left, right = 1, max(dist)
        while left <= right:
            middle = (left + right) // 2
            middle_hour = dist[-1] / middle
            for index in range(len(dist) - 1):
                middle_hour += math.ceil(dist[index] / middle)

            if middle_hour > hour:
                left = middle + 1
            else:
                right = middle - 1
        return left
