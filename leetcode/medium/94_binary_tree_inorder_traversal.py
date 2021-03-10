# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []

        values = []
        if root.left is not None:
            values += self.inorderTraversal(root.left)
        values.append(root.val)
        if root.right is not None:
            values += self.inorderTraversal(root.right)

        return values
