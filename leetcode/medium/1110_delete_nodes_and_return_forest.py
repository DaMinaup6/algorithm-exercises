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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []

        to_delete_set = set(to_delete)
        roots = set([root])
        def helper(parent, node):
            if node is None:
                return

            if node.val in to_delete_set:
                if node in roots:
                    roots.remove(node)
                if node.left:
                    roots.add(node.left)
                if node.right:
                    roots.add(node.right)
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
            helper(node, node.left)
            helper(node, node.right)

        helper(None, root)
        return roots
