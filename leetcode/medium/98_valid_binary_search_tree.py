# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def is_valid_bst(self, node, min_bound, max_bound):
        left_child_valid  = node.left  is None or (node.left.val  < node.val and min_bound < node.left.val  < max_bound)
        right_child_valid = node.right is None or (node.right.val > node.val and min_bound < node.right.val < max_bound)
        if not left_child_valid or not right_child_valid:
            return False

        left_valid  = node.left  is None or self.is_valid_bst(node.left,  min_bound, min(max_bound, node.val))
        right_valid = node.right is None or self.is_valid_bst(node.right, max(min_bound, node.val), max_bound)

        return left_valid and right_valid

    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, -float('inf'), float('inf'))
