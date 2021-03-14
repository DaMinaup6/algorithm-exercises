# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        p_array = [-1] * numCourses
        for prerequisite in prerequisites:
            if prerequisite[0] == prerequisite[1]:
                return False
            if p_array[prerequisite[1]] == -1:
                p_array[prerequisite[1]] = set([prerequisite[0]])
            else:
                p_array[prerequisite[1]].add(prerequisite[0])

        return not any(self.has_cycle(p_array, None, index, 0) for index in range(numCourses))

    def has_cycle(self, p_array, prev_index, start_index, steps):
        if p_array[start_index] == -1:
            return False
        if prev_index in p_array[start_index] or steps > len(p_array):
            return True
        for index in p_array[start_index]:
            if self.has_cycle(p_array, start_index, index, steps + 1):
                return True

        return False

# -----------------------------------------
# Topological sorting with BFS
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegrees = defaultdict(list), defaultdict(int)

        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1

        for _ in range(numCourses):
            has_zero_indegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    has_zero_indegree = True
                    break
            if not has_zero_indegree:
                return False
            indegrees[j] = -1

            for node in graph[j]:
                indegrees[node] -= 1

        return True

# -----------------------------------------
# DFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=EgI5nU9etnU
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i: [] for i in range(numCourses) }
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        visit_set = set()
        def dfs(course):
            if course in visit_set:
                return False
            if len(pre_map[course]) == 0:
                return True

            visit_set.add(course)
            for prerequisite in pre_map[course]:
                if not dfs(prerequisite):
                    return False
            visit_set.remove(course)
            pre_map[course] = []

            return True

        return all(dfs(course) for course in range(numCourses))

# -----------------------------------------
# Detect Cycle in Directed Graph Algorithm
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=rKQaZuoUR4M
# Note: basically this is same as last solution but just try to implement it with white, gray and black set
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prerequisite_map = defaultdict(list)
        for course, prerequisite in prerequisites:
            course_prerequisite_map[course].append(prerequisite)

        unvisited_set, visiting_set, visited_set = set(course_prerequisite_map.keys()), set(), set()
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

            return True

        while len(unvisited_set) > 0:
            course = unvisited_set.pop()
            if not dfs(course):
                return False

        return True
