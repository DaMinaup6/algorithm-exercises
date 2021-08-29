# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n * 2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
# n := len(tasks)
#
# Ref: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1431829/Python-dynamic-programming-on-subsets-explained

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        @lru_cache(None)
        def dp(curr_tasks_status):
            if curr_tasks_status == 0:
                return (1, 0)

            ans = (float('inf'), float('inf'))
            for index in range(len(tasks)):
                if curr_tasks_status & (1 << index):
                    work_sessions, work_time = dp(curr_tasks_status - (1 << index))
                    if work_time + tasks[index] > sessionTime:
                        work_sessions += 1
                        work_time = tasks[index]
                    else:
                        work_time += tasks[index]
                    ans = min(ans, (work_sessions, work_time))

            return ans

        return dp((1 << len(tasks)) - 1)[0]
