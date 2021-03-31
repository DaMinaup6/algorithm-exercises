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
# Ref: https://www.youtube.com/watch?v=53aOi0Drp9I
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pre_val_index_map  = {}
        post_val_index_map = {}
        for index in range(len(post)):
            pre_val_index_map[pre[index]]   = index
            post_val_index_map[post[index]] = index

        def build(left, right):
            if left > right:
                return None
            root = TreeNode(post[right])
            if left == right:
                return root

            left_root_val = pre[pre_val_index_map[root.val] + 1] # in preorder, the value after root value is left root value
            left_root_post_idx = post_val_index_map[left_root_val]
            root.right = build(left_root_post_idx + 1, right - 1)
            root.left  = build(left, left_root_post_idx)
            return root

        return build(0, len(post) - 1)
