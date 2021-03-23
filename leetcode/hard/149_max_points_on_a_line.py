# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points_num = 2
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]

                points_num = 2
                for k in range(len(points)):
                    if k != i and k != j and self.p_on_same_line(p1, p2, points[k]):
                        points_num += 1
                max_points_num = max(max_points_num, points_num)
        
        return max_points_num

    def p_on_same_line(self, p1, p2, p):
        if p1[0] == p2[0]:
            return p[0] == p1[0]
        if p1[1] == p2[1]:
            return p[1] == p1[1]

        return (p[0] - p1[0]) / (p2[0] - p1[0]) == (p[1] - p1[1]) / (p2[1] - p1[1])
