# -----------------------------------------
# My Solution: Priority Queue
#
# Time  Complexity: O(mlog(n))
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(tasks), n := len(servers)
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available_servers = []
        for server_index, server_weight in enumerate(servers):
            heapq.heappush(available_servers, (server_weight, server_index))

        processing_servers = []
        def free_processing_servers(curr_second):
            while len(processing_servers) > 0 and processing_servers[0][0] <= curr_second:
                _, server_weight, server_index = heapq.heappop(processing_servers)
                heapq.heappush(available_servers, (server_weight, server_index))

        curr_second  = 0
        task_pointer = 0
        ans = []
        while len(ans) < len(tasks):
            free_processing_servers(curr_second)
            if len(available_servers) == 0:
                curr_second = processing_servers[0][0]
                free_processing_servers(curr_second)

            # task_pointer also means available start time of some task, i.e. tasks[i] only available for processing after current time reaches second i
            while len(ans) < len(tasks) and len(available_servers) > 0 and curr_second >= task_pointer:
                server_weight, server_index = heapq.heappop(available_servers)
                ans.append(server_index)
                heapq.heappush(processing_servers, (curr_second + tasks[task_pointer], server_weight, server_index))
                task_pointer += 1
            curr_second += 1
        return ans
