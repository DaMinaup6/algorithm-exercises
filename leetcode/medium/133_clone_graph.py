# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# -----------------------------------------
# My Solution: BFS
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V)
# -----------------------------------------
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        new_head = Node(node.val)
        old_new_node_mapping = {node: new_head}

        nodes = deque([(node, new_head)])
        while len(nodes) > 0:
            original_node, new_node = nodes.popleft()
            if len(new_node.neighbors) < len(original_node.neighbors):
                for original_neighbor in original_node.neighbors:
                    if original_neighbor not in old_new_node_mapping:
                        new_neighbor = Node(original_neighbor.val)
                        old_new_node_mapping[original_neighbor] = new_neighbor
                    else:
                        new_neighbor = old_new_node_mapping[original_neighbor]

                    new_node.neighbors.append(new_neighbor)
                    nodes.append((original_neighbor, new_neighbor))

        return new_head

# -----------------------------------------
# DFS
#
# Time  Complexity: O(V + E)
# Space Complexity: O(V)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/88363919
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_new_node_mapping = {}
        def deep_clone(old_node):
            if old_node is None:
                return None
            if old_node in old_new_node_mapping:
                return old_new_node_mapping[old_node]

            new_node = Node(old_node.val)
            old_new_node_mapping[old_node] = new_node
            for neighbor in old_node.neighbors:
                new_neighbor = deep_clone(neighbor)
                if new_neighbor is not None:
                    new_node.neighbors.append(new_neighbor)

            return new_node

        return deep_clone(node)
