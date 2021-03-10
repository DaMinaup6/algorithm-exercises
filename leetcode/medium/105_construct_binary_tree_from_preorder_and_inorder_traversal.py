# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 0:
            return root

        inorder_root_idx = inorder.index(preorder[0])
        left_inorder  = inorder[:(inorder_root_idx)]
        right_inorder = inorder[(inorder_root_idx + 1):]

        left_inorder_set = set(left_inorder)
        left_preorder, right_preorder = [], []
        for value in preorder[1:]:
            if value in left_inorder_set:
                left_preorder.append(value)
            else:
                right_preorder.append(value)

        root.left  = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
class Solution:
    def buildTree(self, preorder, inorder):
        preorder_currsor  = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        def array_to_tree(left, right):
            nonlocal preorder_currsor

            if left > right:
                return None

            root = TreeNode(preorder[preorder_currsor])
            preorder_currsor += 1

            root.left  = array_to_tree(left, inorder_index_map[root.value] - 1)
            root.right = array_to_tree(inorder_index_map[root.value] + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
