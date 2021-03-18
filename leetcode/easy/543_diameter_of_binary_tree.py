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

from functools import lru_cache

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        @lru_cache(None)
        def helper(node, parent_selected, path_length):
            if node is None:
                return path_length

            if parent_selected:
                left_length, right_length = 0, 0
                if node.left:
                    left_length = helper(node.left, True, path_length + 1)
                if node.right:
                    right_length = helper(node.right, True, path_length + 1)

                return max(path_length, left_length, right_length)
            else:
                go_left_length, left_length, go_right_length, right_length = 0, 0, 0, 0
                if node.left:
                    go_left_length = helper(node.left, False, 0)
                    left_length = helper(node.left, True, path_length + 1)
                if node.right:
                    go_right_length = helper(node.right, False, 0)
                    right_length = helper(node.right, True, path_length + 1)

                return max(path_length, go_left_length, go_right_length, left_length + right_length)

        return helper(root, False, 0)

# -----------------------------------------
# DFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/diameter-of-binary-tree/solution/
# Note: similar to 124_binary_tree_maximum_path_sum.py
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        def calc_diameter(node):
            nonlocal diameter

            if node is None:
                return 0

            left_diameter  = calc_diameter(node.left)
            right_diameter = calc_diameter(node.right)

            diameter = max(diameter, left_diameter + right_diameter)
            return max(left_diameter, right_diameter) + 1

        calc_diameter(root)
        return diameter
