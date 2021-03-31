# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sorted_A = sorted(A)
        sorted_B = sorted(B)        
        num_indexes_map = defaultdict(list)
        for index in range(len(B)):
            num_indexes_map[B[index]].append(index)

        output = [-1] * len(B)
        for index in range(len(B) - 1, -1, -1):
            if sorted_A[-1] > sorted_B[index]:
                output_index = num_indexes_map[sorted_B[index]].pop()
                output[output_index] = sorted_A.pop()
        if len(sorted_A) > 0:
            for index in range(len(B) - 1, -1, -1):
                if output[index] == -1:
                    output[index] = sorted_A.pop()
        return output

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82796298
from collections import deque

class Solution(object):
    def advantageCount(self, A, B):
        A = deque(sorted(A))
        B = deque(sorted((num, index) for index, num in enumerate(B)))

        output = [-1] * len(A)
        for _ in range(len(A)):
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            output[b[1]] = a
        return output
