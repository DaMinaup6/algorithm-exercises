# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n) + n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(intervals)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals, key=lambda interval: (interval[0], interval[1]))

        curr_interval = intervals[0]
        removed_count = 0
        for index in range(1, len(intervals)):
            interval = intervals[index]
            if curr_interval[0] <= interval[0] < curr_interval[1]:
                removed_count += 1
                # e.g. intervals == [[-100, 1], [-99, -98], [-97, 2]]
                # [-100, 1] overlaps with [-99, -98], remove the one with further right margin
                # so there would be less chance for comming intervals overlaps with current interval
                if curr_interval[1] > interval[1]:
                    curr_interval = interval
            elif interval[0] == curr_interval[1]:
                curr_interval[1] = interval[1]
            else:
                curr_interval = interval

        return removed_count
