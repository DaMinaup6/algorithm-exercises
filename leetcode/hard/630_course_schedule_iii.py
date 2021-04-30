# -----------------------------------------
# Model Solution: Greddy + Heap
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: (course[1], course[0]))

        durations = []
        curr_time = 0
        for course in courses:
            # If curr_time add current duration (course[0]) would exceed current deadline, which means we cannot finish all courses so far,
            # we need at least drop one course
            if curr_time + course[0] > course[1]:
                # If the current duration is less than the biggest duration so far, replace the class with biggest duration with current course
                # then the total duration would be reduced
                if len(durations) > 0 and course[0] < -durations[0]:
                    prev_duration = -heapq.heappop(durations)
                    heapq.heappush(durations, -course[0])
                    curr_time -= prev_duration - course[0]
            else:
                heapq.heappush(durations, -course[0])
                curr_time += course[0]

        return len(durations)
