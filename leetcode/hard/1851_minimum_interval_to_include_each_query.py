# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mlog(m) + nlog(n))
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(queries), n := len(intervals)
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals, reverse=True)

        interval_heap  = []
        interval_sizes = {}
        for query in sorted(queries):
            while len(intervals) > 0 and intervals[-1][0] <= query:
                start, end = intervals.pop()
                if end >= query:
                    heapq.heappush(interval_heap, (end - start + 1, end))

            while len(interval_heap) > 0 and interval_heap[0][1] < query:
                heapq.heappop(interval_heap)

            interval_sizes[query] = interval_heap[0][0] if len(interval_heap) > 0 else -1

        return [interval_sizes[query] for query in queries]
