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
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder_treversal(node):
            if node is None:
                return []

            nodes = []
            nodes.append(node)
            if node.left is not None:
                nodes += preorder_treversal(node.left)
            if node.right is not None:
                nodes += preorder_treversal(node.right)
            return nodes
        nodes = preorder_treversal(root)

        for index in range(len(nodes) - 1):
            node = nodes[index]
            node.left  = None
            node.right = nodes[index + 1]
