# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
# n := len(A) == len(B) == len(C) == len(D)
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = []
        for num_a in A:
            for num_b in B:
                AB.append(num_a + num_b)
        CD = defaultdict(int)
        for num_c in C:
            for num_d in D:
                CD[num_c + num_d] += 1

        ans = 0
        for num in AB:
            if -num in CD:
                ans += CD[-num]
        return ans

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(A) == len(B) == len(C) == len(D)
# Ref: https://blog.csdn.net/danspace1/article/details/87854254
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB_sum = defaultdict(int)
        for num_a in A:
            for num_b in B:
                AB_sum[num_a + num_b] += 1
        return sum(AB_sum[-(num_c + num_d)] for num_c in C for num_d in D)
