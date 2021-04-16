'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
'''

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V + E)
# -----------------------------------------
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n, edges):
        connted_graph = defaultdict(list)
        for edge in edges:
            connted_graph[edge[0]].append(edge[1])
            connted_graph[edge[1]].append(edge[0])

        visited_nodes = set()
        components_count = 0
        def dfs(node):
            if node in visited_nodes:
                return
            visited_nodes.add(node)
            for neighbor in connted_graph[node]:
                dfs(neighbor)

        for node in range(n):
            if node not in visited_nodes:
                dfs(node)
                components_count += 1

        return components_count

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(V + Elog(V))
# Space Complexity: O(V)
# -----------------------------------------
# Ref:
# a) https://www.youtube.com/watch?v=ymxPZk7TesQ
# b) https://youtu.be/K5gYn7qL3lE?t=186
class Solution:
    def countComponents(self, n, edges):
        union_root = list(range(n))
        def find_union_root(node):
            if node != union_root[node]:
                union_root[node] = find_union_root(union_root[union_root[node]])
            return union_root[node]

        # initially, we have n connected path
        components_count = n 
        def union(node_1, node_2):
            nonlocal components_count
            # find root of node_1
            root_1 = find_union_root(node_1)
            # find root of node_2
            root_2 = find_union_root(node_2)
            # if roots of node_1 and node_2 are not identical, merge them
            if root_1 != root_2:
                union_root[root_1] = root_2
                components_count -= 1

        # store original roots
        root = [num for num in range(n)] 
        # go through each node pair
        for edge in edges:
            union(edge[0], edge[1])
        return components_count

processor = Solution()
print(f"processor.countComponents(5, [[0, 1], [1, 2], [3, 4]])         == 2: {processor.countComponents(5, [[0, 1], [1, 2], [3, 4]])         == 2}")
print(f"processor.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1: {processor.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1}")
