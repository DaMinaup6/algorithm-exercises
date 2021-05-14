# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(m)
# -----------------------------------------
# m := sum(wall[0]), n := sum(len(wall[i]))
import collections

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cut_lines_count = collections.defaultdict(int)
        max_count = 0
        # e.g. wall == [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
        # check brick by brick, calculate cumulative sum and we can find out that there are three arrays in wall contains cumulative sum 4
        # answer would be len(wall) - max_count
        for bricks in wall:
            pre_sum = 0
            for index in range(len(bricks) - 1):
                pre_sum += bricks[index]
                cut_lines_count[pre_sum] += 1
                max_count = max(max_count, cut_lines_count[pre_sum])

        return len(wall) - max_count
