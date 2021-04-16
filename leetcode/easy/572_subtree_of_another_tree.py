# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := number of nodes in t, n := number of nodes in s
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        return self.is_same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        return s.val == t.val and self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := number of nodes in t, n := number of nodes in s
# Ref: https://leetcode.com/problems/subtree-of-another-tree/discuss/1130997/Python-or-O(n)-or-super-easy-to-understand
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def hashify(node):
            if node is None:
                return
            key = (node.val, hashify(node.left), hashify(node.right))
            return tree_node_id_mapping.setdefault(key, len(tree_node_id_mapping))

        tree_node_id_mapping = {}
        hashify(s)
        return (t.val, hashify(t.left), hashify(t.right)) in tree_node_id_mapping
