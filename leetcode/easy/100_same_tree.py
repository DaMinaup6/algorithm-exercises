# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------

# -----> Version 1
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_nodes = [p]
        q_nodes = [q]
        while len(p_nodes) > 0 and len(q_nodes) > 0:
            if len(p_nodes) != len(q_nodes):
                return False

            new_p_nodes = []
            new_q_nodes = []
            for index in range(len(p_nodes)):
                p_node = p_nodes[index]
                q_node = q_nodes[index]
                if p_node is None and q_node is None:
                    continue
                elif p_node is None or q_node is None or p_node.val != q_node.val:
                    return False
                else:
                    new_p_nodes.extend([p_node.left, p_node.right])
                    new_q_nodes.extend([q_node.left, q_node.right])

            p_nodes = new_p_nodes
            q_nodes = new_q_nodes

        return True

# -----> Version 2
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        nodes = deque([(p, q)])
        while len(nodes) > 0:
            p_node, q_node = nodes.popleft()
            if p_node is None and q_node is None:
                continue
            elif p_node is None or q_node is None or p_node.val != q_node.val:
                return False
            else:
                nodes.append((p_node.left, q_node.left))
                nodes.append((p_node.right, q_node.right))

        return True

# -----------------------------------------
# Recursion
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
