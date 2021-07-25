# -----------------------------------------
# Model Solution: Line Sweep
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(segments)
#
# Ref: https://leetcode.com/problems/describe-the-painting/discuss/1359720/Line-Sweep
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        point_color_mix = defaultdict(int)
        for start, end, color in segments:
            point_color_mix[start] += color
            point_color_mix[end] -= color

        points = sorted(point_color_mix.keys())
        painting, prev_point = [], points[0]
        for curr_point in points[1:]:
            if point_color_mix[prev_point] > 0:
                painting.append([prev_point, curr_point, point_color_mix[prev_point]])
                point_color_mix[curr_point] += point_color_mix[prev_point]
            prev_point = curr_point

        return painting
