# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_axis_points_count = defaultdict(list)
        y_axis_points_count = defaultdict(list)
        for x, y in stones:
            x_axis_points_count[x].append((x, y))
            y_axis_points_count[y].append((x, y))

        # find "connected" points and add its size - 1, i.e. for points [(1, 0), (1, 1), (2, 1)], they are connected and
        # for points [(0, 0), (1, 1)], they are not connected
        #
        # for all groups of points, the max number of points to remove for each group is group size - 1
        max_stones_remove = 0
        checked_points = set()
        for x, y in stones:
            if (x, y) in checked_points:
                continue

            group_points_count = 0
            group_points = set([(x, y)])
            while len(group_points) > 0:
                group_points_count += len(group_points)

                points_to_generate_next_points = set()
                for x, y in group_points:
                    if (x, y) in checked_points:
                        continue
                    checked_points.add((x, y))
                    points_to_generate_next_points.add((x, y))

                next_points = set()
                for x, y in points_to_generate_next_points:
                    for next_point in x_axis_points_count[x] + y_axis_points_count[y]:
                        if next_point not in checked_points:
                            next_points.add(next_point)
                group_points = next_points

            max_stones_remove += group_points_count - 1
        return max_stones_remove
