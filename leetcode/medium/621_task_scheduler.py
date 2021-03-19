# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/81947087

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = collections.Counter(tasks)
        most = task_counter.most_common()[0][1]
        most_task_num = len([task for task, task_count in task_counter.items() if task_count == most])
        if most_task_num >= n + 1:
            return len(tasks)

        return (most - 1) * (n + 1) + most_task_num
