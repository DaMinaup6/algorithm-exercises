# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=8JM_dyOu_JY
from collections import defaultdict

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points_count = defaultdict(int)
        total_area = 0
        for rectangle in rectangles:
            total_area += (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])
            for point in [(rectangle[0], rectangle[1]), (rectangle[2], rectangle[1]), (rectangle[0], rectangle[3]), (rectangle[2], rectangle[3])]:
                points_count[point] += 1
                if points_count[point] > 1:
                    points_count.pop(point)

        # if all the rectangles together form an exact cover of a rectangular region, there are only 4 points appear once, which are corners
        if len(points_count) != 4:
            return False
        # make sure the area formed by four corners equals area of all rectangles
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
        for point in points_count:
            min_x = min(min_x, point[0])
            min_y = min(min_y, point[1])
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
        return total_area == (max_x - min_x) * (max_y - min_y)
