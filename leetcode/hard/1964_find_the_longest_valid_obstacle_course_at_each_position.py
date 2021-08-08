# -----------------------------------------
# My Solution: Patience Sorting
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(obstacles)

import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        course_sequence = [obstacles[0]]
        ans = [1]
        for index in range(1, len(obstacles)):
            if len(course_sequence) == 0 or course_sequence[-1] <= obstacles[index]:
                course_sequence.append(obstacles[index])
                ans.append(len(course_sequence))
            else:
                bisect_index = bisect.bisect_right(course_sequence, obstacles[index])
                course_sequence[bisect_index] = obstacles[index]
                ans.append(bisect_index + 1)

        return ans
