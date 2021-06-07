# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms
from itertools import combinations

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for x, y in points:
            points_set.add((x, y))

        min_area = float('inf')
        for (x_1, y_1), (x_2, y_2) in combinations(points, 2):
            if x_1 != x_2 and y_1 != y_2 and (x_1, y_2) in points_set and (x_2, y_1) in points_set:
                curr_area = abs(x_1 - x_2) * abs(y_1 - y_2)
                min_area  = min(min_area, curr_area)
        return min_area if min_area != float('inf') else 0
