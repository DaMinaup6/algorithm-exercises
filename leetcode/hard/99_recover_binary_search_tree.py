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
        # For example 1:
        #   1
        #  /
        # 3
        #  \
        #   2
        # the inorder traversal would be [3, 2, 1]
        # when we find first element greater than its next element, which is 3 in this case, we record 3 in sefl.node_1
        # then we find last element smaller than its previous element, which is 1 in this case, record 1 in sefl.node_2
        # swap sefl.node_1 and sefl.node_2 then we fix this tree
        #
        # One more example: [1, 5, 3, 4, 2]
        # 5 is the first element greater than its next element and 2 is the last element smaller than its previous element
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
