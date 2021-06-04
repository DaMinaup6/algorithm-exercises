# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://blog.csdn.net/fuxuemingzhu/article/details/100828798
# b) https://www.youtube.com/watch?v=2SXqBsTR6a8
# c) https://www.educative.io/edpresso/tuples-vs-list-in-python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # store tuple would use less memory and the speed of creation is faster. Ref: https://www.educative.io/edpresso/tuples-vs-list-in-python
        queue  = deque() # [(index, num)]
        output = []

        for index, num in enumerate(nums):
            if len(queue) > 0 and index - queue[0][0] == k:
                queue.popleft()
            while len(queue) > 0 and queue[-1][1] <= num:
                queue.pop()
            queue.append((index, num))

            if index >= k - 1:
                output.append(queue[0][1])

        return output
