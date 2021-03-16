'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30], [5, 10], [15, 20]]
Output: 2

Example 2:

Input: [[7, 10], [2, 4]]
Output: 1

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://blog.csdn.net/danspace1/article/details/86076499
# b) https://www.youtube.com/watch?v=4MEkBvqE_2Q
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0

        intervals.sort()
        pq = []
        for interval in intervals:
            # room is already used in last meeting and continue to use the same room for this meeting
            if len(pq) > 0 and interval[0] >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])

        return len(pq)

processor = Solution()
print(f"processor.minMeetingRooms([[5, 10], [0, 30], [15, 20]]) == 2: {processor.minMeetingRooms([[5, 10], [0, 30], [15, 20]]) == 2}")
print(f"processor.minMeetingRooms([[7, 10], [2, 4]])            == 1: {processor.minMeetingRooms([[7, 10], [2, 4]]) == 1}")
