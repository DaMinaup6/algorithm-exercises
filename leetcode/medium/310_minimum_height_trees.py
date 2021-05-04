# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-height-trees/
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        node_edges = collections.defaultdict(set)
        for edge in edges:
            node_edges[edge[0]].add(edge[1])
            node_edges[edge[1]].add(edge[0])

        leaves = collections.deque()
        for node in node_edges:
            if len(node_edges[node]) == 1:
                leaves.append(node)

        remaining_nodes = n
        while remaining_nodes > 2:
            curr_leaves_size = len(leaves)
            remaining_nodes -= curr_leaves_size
            for _ in range(curr_leaves_size):
                curr_leaf = leaves.popleft()
                leaf_parent = node_edges[curr_leaf].pop()

                node_edges[leaf_parent].remove(curr_leaf)
                if len(node_edges[leaf_parent]) == 1:
                    leaves.append(leaf_parent)

        return leaves
