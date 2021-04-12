# -----------------------------------------
# My Solution
#
# Time  Complexity: O(2n + 2log(n))
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # Time Complexity: O(2log(n))
        self.intervals = intervals
        left_position  = self.find_left_position(newInterval[0])
        if left_position == len(intervals):
            if newInterval[0] == intervals[-1][1]:
                return intervals[:-1] + [[intervals[-1][0], newInterval[1]]]
            return intervals + [newInterval]
        right_position = self.find_right_position(newInterval[1])
        if right_position == -1:
            if newInterval[1] == intervals[0][0]:
                return [[newInterval[0], intervals[0][1]]] + intervals[1:]
            return [newInterval] + intervals

        # Time Complexity: O(2n)
        return intervals[:left_position] + [[min(intervals[left_position][0], newInterval[0]), max(intervals[right_position][1], newInterval[1])]] + intervals[(right_position + 1):]
    
    def find_left_position(self, left_val):
        if left_val >= self.intervals[-1][1]:
            return len(self.intervals)
        if left_val <= self.intervals[0][1]:
            return 0

        left  = 0
        right = len(self.intervals) - 1
        while left < right:
            middle = (left + right) // 2
            if middle > 0 and self.intervals[middle - 1][1] < left_val <= self.intervals[middle][1]:
                return middle
            elif self.intervals[middle][0] < left_val:
                left = middle + 1
            else:
                right = middle - 1

        return left
    
    def find_right_position(self, right_val):
        if right_val <= self.intervals[0][0]:
            return -1
        if right_val >= self.intervals[-1][0]:
            return len(self.intervals) - 1

        left  = 0
        right = len(self.intervals) - 1
        while left < right:
            middle = (left + right) // 2
            if middle < len(self.intervals) - 1 and self.intervals[middle][0] <= right_val < self.intervals[middle + 1][0]:
                return middle
            elif self.intervals[middle][1] < right_val:
                left = middle + 1
            else:
                right = middle - 1

        return left

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://maxming0.github.io/2020/09/13/Insert-Interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        output = []
        cursor = 0
        while cursor < len(intervals) and intervals[cursor][1] < newInterval[0]:
            output.append(intervals[cursor])
            cursor += 1
        while cursor < len(intervals) and intervals[cursor][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[cursor][0])
            newInterval[1] = max(newInterval[1], intervals[cursor][1])
            cursor += 1

        return output + [newInterval] + intervals[cursor:]
