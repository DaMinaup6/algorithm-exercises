# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79672901
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.prev, self.node_1, self.node_2 = None, None, None
        self.in_order(root)
        self.node_1.val, self.node_2.val = self.node_2.val, self.node_1.val

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)
        if self.prev is not None and self.prev.val > root.val:
            if self.node_1 is None:
                self.node_1 = self.prev
            self.node_2 = root
        self.prev = root
        self.in_order(root.right)
