# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V + E)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) == 0:
            return True
        colors = [0] * len(graph)
        queue  = deque()
        
        for node in range(len(graph)):
            if colors[node] == 0:
                colors[node] = 1
                queue.append(node)
            
            while len(queue) > 0:
                curr_node = queue.popleft()
                for neighbor in graph[curr_node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = 1 if colors[curr_node] == 2 else 2
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[curr_node]:
                        return False
        return True
