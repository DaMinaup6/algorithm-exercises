# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            right_min_node = self.find_min_node(root.right)
            right_min_node.left = root.left
            return root.right
        elif root.left and root.left.val == key:
            if root.left.right is None:
                root.left = root.left.left
            else:
                left_right_min = self.find_min_node(root.left.right)
                left_right_min.left = root.left.left
                root.left = root.left.right
        elif root.right and root.right.val == key:
            if root.right.left is None:
                root.right = root.right.right
            else:
                right_left_max = self.find_max_node(root.right.left)
                right_left_max.right = root.right.right
                root.right = root.right.left
        elif root.val > key:
            self.deleteNode(root.left, key)
        elif root.val < key:
            self.deleteNode(root.right, key)

        return root

    def find_min_node(self, root: TreeNode) -> TreeNode:
        if root is None or root.left is None:
            return root
        return self.find_min_node(root.left)

    def find_max_node(self, root: TreeNode) -> TreeNode:
        if root is None or root.right is None:
            return root
        return self.find_max_node(root.right)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79670068
class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            if root.right is None:
                return root.left
            else:
                right_min_node = root.right
                while right_min_node.left:
                    right_min_node = right_min_node.left

                root.val, right_min_node.val = right_min_node.val, root.val
                root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root
