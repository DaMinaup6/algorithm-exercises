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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        num_set = set()
        def preorder(node):
            if node is None:
                return False

            num_set.add(node.val)
            if node.val * 2 != k and k - node.val in num_set:
                return True
            return preorder(node.left) or preorder(node.right)

        return preorder(root)
