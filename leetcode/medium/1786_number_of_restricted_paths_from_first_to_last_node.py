# Ref:
# a) https://www.youtube.com/watch?v=ukav97j7wOI
# b) https://www.youtube.com/watch?v=pVfj6mxhdMw
# c) https://www.youtube.com/watch?v=YMyO-yZMQ6g

from collections import defaultdict
from functools   import lru_cache
import heapq

class Solution:
    def countRestrictedPaths(self, n, edges):
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        distance_to_last_node = [float('inf') for _ in range(n + 1)]
        distance_to_last_node[n] = 0

        visited_nodes = set()
        pq = [(0, n)]
        while pq:
            distance, node = heapq.heappop(pq)
            visited_nodes.add(node)

            for (neighbor, weight) in graph[node]:
                if neighbor not in visited_nodes:
                    new_distance = distance + weight
                    if new_distance < distance_to_last_node[neighbor]:
                        heapq.heappush(pq, (new_distance, neighbor))
                        distance_to_last_node[neighbor] = new_distance

        @lru_cache(None)
        def dp(node):
            if node == n:
                return 1
            path_num = 0
            for (neighbor, weight) in graph[node]:
                if distance_to_last_node[node] > distance_to_last_node[neighbor]:
                    path_num += dp(neighbor)
            return path_num

        return dp(1) % (10 ** 9 + 7)

processor = Solution()

input_1 = [[1, 5, 10], [1, 2, 1], [2, 5, 1], [1, 3, 1], [3, 5, 1], [1, 4, 1], [4, 5, 1]]
input_2 = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]
input_3 = [[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2], [7, 5, 3], [2, 6, 4]]
input_4 = [[6, 2, 35129], [3, 4, 99499], [2, 7, 43547], [8, 1, 78671], [2, 1, 66308], [9, 6, 33462], [5, 1, 48249], [2, 3, 44414], [6, 7, 44602], [1, 7, 14931], [8, 9, 38171], [4, 5, 30827], [3, 9, 79166], [4, 8, 93731], [5, 9, 64068], [7, 5, 17741], [6, 3, 76017], [9, 4, 72244]]
input_5 = [[6, 2, 5], [2, 4, 10], [10, 2, 1], [9, 3, 1], [1, 5, 6], [8, 7, 3], [7, 10, 3], [5, 4, 2], [4, 7, 2], [9, 5, 7], [8, 9, 10], [10, 6, 4], [4, 8, 4], [6, 3, 9], [1, 9, 9], [3, 5, 7], [5, 2, 2]]
print(f"processor.countRestrictedPaths( 5, input_1) == 4: {processor.countRestrictedPaths( 5, input_1) == 4}")
print(f"processor.countRestrictedPaths( 5, input_2) == 3: {processor.countRestrictedPaths( 5, input_2) == 3}")
print(f"processor.countRestrictedPaths( 7, input_3) == 1: {processor.countRestrictedPaths( 7, input_3) == 1}")
print(f"processor.countRestrictedPaths( 9, input_4) == 6: {processor.countRestrictedPaths( 9, input_4) == 6}")
print(f"processor.countRestrictedPaths(10, input_5) == 1: {processor.countRestrictedPaths(10, input_5) == 1}")
