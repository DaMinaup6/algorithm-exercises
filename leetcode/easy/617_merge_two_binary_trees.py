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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None or root2 is None:
            return root1 or root2

        merged_root = TreeNode(root1.val + root2.val)
        merged_root.left  = self.mergeTrees(root1.left,  root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)

        return merged_root

# -----------------------------------------
# Enhanced Solution (not create new root)
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None or root2 is None:
            return root1 or root2

        root1.val  += root2.val
        root1.left  = self.mergeTrees(root1.left,  root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
