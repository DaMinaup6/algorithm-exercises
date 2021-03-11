# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val    = int(x)
        self.next   = next
        self.random = random

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        # create new nodes and node -> index mapping
        new_nodes = []
        node_index_dict = {}
        node_index = 0
        node = head
        while node is not None:
            new_node = Node(node.val)
            new_nodes.append(new_node)
            if node_index > 0:
                new_nodes[node_index - 1].next = new_node

            node_index_dict[node] = node_index

            node_index += 1
            node = node.next

        # use node -> index mapping to find out the index node.random points to
        random_index_list = []
        node = head
        while node is not None:
            random_index_list.append(node_index_dict[node.random] if node.random is not None else None)
            node = node.next

        # assign random to new nodes
        for index, new_node in enumerate(new_nodes):
            if random_index_list[index] is not None:
                new_node.random = new_nodes[random_index_list[index]]

        return new_nodes[0]
