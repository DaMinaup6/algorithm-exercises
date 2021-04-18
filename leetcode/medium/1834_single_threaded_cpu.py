# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index in range(len(tasks)):
            tasks[index].append(index)
        heapq.heapify(tasks)

        curr_time = 0
        pending_tasks = []
        task_schedule = []
        while len(tasks) > 0:
            # heappop will help get shortest processing time for same enque time or smallest index for same process time
            curr_enqueue_time, process_time, task_index = heapq.heappop(tasks)

            # process pending tasks until curr_time achieves or exceeds curr_enqueue_time
            while len(pending_tasks) > 0 and curr_time < curr_enqueue_time:
                pending_task = heapq.heappop(pending_tasks)
                curr_time += pending_task[0]
                task_schedule.append(pending_task[1])

            if curr_time >= curr_enqueue_time:
                heapq.heappush(pending_tasks, (process_time, task_index))
            else: # in this case, len(pending_tasks) must be 0 so no need check if there is still any pending task remaining
                curr_time = curr_enqueue_time + process_time
                task_schedule.append(task_index)

        while len(pending_tasks) > 0:
            pending_task = heapq.heappop(pending_tasks)
            task_schedule.append(pending_task[1])

        return task_schedule
