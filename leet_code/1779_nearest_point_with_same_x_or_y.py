# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def nearestValidPoint(self, x, y, points):
        min_manhattan_distance = float('inf')
        nearest_point_index    = -1

        for point_index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                manhattan_distance = abs(x - point[0]) + abs(y - point[1])
                if manhattan_distance < min_manhattan_distance:
                    min_manhattan_distance = manhattan_distance
                    nearest_point_index    = point_index

        return nearest_point_index
