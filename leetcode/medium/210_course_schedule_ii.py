# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V + E)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=rKQaZuoUR4M
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))
        
        course_prerequisite_map = defaultdict(list)
        for course, prerequisite in prerequisites:
            course_prerequisite_map[course].append(prerequisite)
        
        unvisited_set, visiting_set, visited_set = set(course_prerequisite_map.keys()), set(), set()
        courses_order = []
        def dfs(course):
            if course in visited_set:
                return True
            if course in visiting_set:
                return False

            visiting_set.add(course)
            for prerequisite in course_prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False
            visiting_set.remove(course)
            visited_set.add(course)
            courses_order.append(course)

            return True

        while len(unvisited_set) > 0:
            course = unvisited_set.pop()
            if not dfs(course):
                return []

        for course in range(numCourses):
            if course not in visited_set:
                courses_order.append(course)
        return courses_order
