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
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=6cA_NDtpyz8
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = -float('inf')

        def path_sum(node: TreeNode) -> int:
            nonlocal max_path_sum

            if node is None:
                return 0

            left_sum  = max(0, path_sum(node.left))
            right_sum = max(0, path_sum(node.right))

            max_path_sum = max(max_path_sum, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val

        path_sum(root)
        return max_path_sum
