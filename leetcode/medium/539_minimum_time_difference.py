# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time_point in timePoints:
            hour, minute = time_point.split(':')
            minutes.append(int(hour) * 60 + int(minute))
        minutes.sort()
        minutes.append(1440 + minutes[0])

        min_diff = float('inf')
        for index in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[index + 1] - minutes[index])
        return min_diff
