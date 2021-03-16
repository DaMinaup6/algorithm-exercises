# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []


    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
        else:
            bisect.insort(self.arr, num)


    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            return self.arr[len(self.arr) // 2]
        else:
            return (self.arr[len(self.arr) // 2] + self.arr[len(self.arr) // 2 - 1]) / 2

# -----------------------------------------
# Model Solution: Two Heaps
#
# Time  Complexity: O(log(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=U_tisGQrQ3c
import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or -self.max_heap[0] > num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)


    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
