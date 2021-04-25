# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^3 + mn^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(dependencies)
import math
import collections
import itertools

class Course:
    def __init__(self):
        self.next_course = None
        self.prerequisites = []

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        if len(dependencies) == 0:
            return math.ceil(n / k)
        if k == 1:
            return n

        courses = collections.defaultdict(Course)
        for prerequisite, course in dependencies:
            prerequisite_object = courses[prerequisite]
            prerequisite_object.next_course = course

            course_object = courses[course]
            course_object.prerequisites.append(prerequisite)
        # for courses not listed in dependencies, they can be taken anytime
        no_dependencies_courses = n - len(courses)

        min_semesters_need = float('inf')
        def dfs(curr_semester, taken_courses):
            nonlocal min_semesters_need, no_dependencies_courses

            if len(taken_courses) == len(courses):
                min_semesters_need = min(min_semesters_need, curr_semester)
            else:
                available_courses = []
                for course in courses:
                    course_object = courses[course]
                    if course not in taken_courses and (len(course_object.prerequisites) == 0 or all(prerequisite in taken_courses for prerequisite in course_object.prerequisites)):
                        available_courses.append(course)

                if len(available_courses) < k:
                    new_taken_courses = taken_courses.copy()
                    new_taken_courses.update(available_courses)
                    # if there are some courses remain, spend the rest on no_dependencies_courses
                    if no_dependencies_courses > 0:
                        no_dependencies_courses -= k - len(available_courses)
                        no_dependencies_courses = max(0, no_dependencies_courses)

                    dfs(curr_semester + 1, new_taken_courses)
                else:
                    # use combination to select courses to take in this semester
                    for courses_to_take in itertools.combinations(available_courses, k):
                        new_taken_courses = taken_courses.copy()
                        new_taken_courses.update(courses_to_take)
                        dfs(curr_semester + 1, new_taken_courses)

        dfs(0, set())
        return min_semesters_need + math.ceil(no_dependencies_courses / k)
