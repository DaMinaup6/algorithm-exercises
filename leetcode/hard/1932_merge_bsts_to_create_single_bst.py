# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(trees)
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        if len(trees) == 1:
            return trees[0]

        root_val_root_mapping = {}
        mergeable_parent_root = {}
        for index, root in enumerate(trees):
            root_val_root_mapping[root.val] = (root, index)
            mergeable_parent_root[root.val] = None

        mergeable_count = 0
        for root in trees:
            if root.left is not None and root.left.val in mergeable_parent_root:
                child_root = root_val_root_mapping[root.left.val][0]
                if self.valid_to_merge_left(root, child_root):
                    if mergeable_parent_root[child_root.val] is not None:
                        return None
                    mergeable_parent_root[child_root.val] = root
                    mergeable_count += 1
            if root.right is not None and root.right.val in mergeable_parent_root:
                child_root = root_val_root_mapping[root.right.val][0]
                if self.valid_to_merge_right(root, child_root):
                    if mergeable_parent_root[child_root.val] is not None:
                        return None
                    mergeable_parent_root[child_root.val] = root
                    mergeable_count += 1
        if mergeable_count != len(trees) - 1:
            return None

        for root_val in mergeable_parent_root:
            root = root_val_root_mapping[root_val][0]
            parent_root = mergeable_parent_root[root_val]
            if parent_root is None:
                continue

            if parent_root.left is not None and parent_root.left.val == root.val:
                parent_root.left = root
                trees[root_val_root_mapping[root.val][1]] = None
            else:
                parent_root.right = root
                trees[root_val_root_mapping[root.val][1]] = None

        for root in trees:
            if root is not None and self.is_valid_bst(root, -float('inf'), float('inf')):
                return root
        return None

    def valid_to_merge_left(self, root, other_root):
        if other_root.val >= root.val:
            return False
        if other_root.left is not None and other_root.left.val >= root.val:
            return False
        if other_root.right is not None and other_root.right.val >= root.val:
            return False
        return True

    def valid_to_merge_right(self, root, other_root):
        if other_root.val <= root.val:
            return False
        if other_root.left is not None and other_root.left.val <= root.val:
            return False
        if other_root.right is not None and other_root.right.val <= root.val:
            return False
        return True

    def is_valid_bst(self, node, min_bound, max_bound):
        left_child_valid  = node.left  is None or (node.left.val  < node.val and min_bound < node.left.val  < max_bound)
        right_child_valid = node.right is None or (node.right.val > node.val and min_bound < node.right.val < max_bound)
        if not left_child_valid or not right_child_valid:
            return False

        left_valid  = node.left  is None or self.is_valid_bst(node.left,  min_bound, min(max_bound, node.val))
        right_valid = node.right is None or self.is_valid_bst(node.right, max(min_bound, node.val), max_bound)

        return left_valid and right_valid
