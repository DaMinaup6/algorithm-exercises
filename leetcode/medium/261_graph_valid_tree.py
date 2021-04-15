'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
'''

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def validTree(self, n, edges):
        connected = defaultdict(list)
        for edge in edges:
            connected[edge[0]].append(edge[1])

        visited_nodes = set()
        def dfs(node):
            for neighbor in connected[node]:
                if neighbor in visited_nodes:
                    return False
                visited_nodes.add(neighbor)
                if not dfs(neighbor):
                    return False

            return True

        visited_nodes.add(edges[0][0])
        if not dfs(edges[0][0]):
            return False
        return len(visited_nodes) == n

processor = Solution()
print(f"processor.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])                 == True:  {processor.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])                 == True}")
print(f"processor.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])         == False: {processor.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])         == False}")
print(f"processor.validTree(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == True:  {processor.validTree(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == True}")
