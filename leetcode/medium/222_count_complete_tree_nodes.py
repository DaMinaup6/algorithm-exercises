# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O((log(n))^2)
# Space Complexity: O(1)
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
# b) https://maxming0.github.io/2020/06/23/Count-Complete-Tree-Nodes/
# Note: since we take O(log(n)) time to calculate size of left or right sub-tree and it takes log(n) iterations
#       so time complexity is O((log(n))^2)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # e.g. root == [1, 2, 3, 4, 5, 6] => left_depth == 2 and right_depth == 2
        #      in this case the left sub-tree is complete
        # e.g. root == [1, 2, 3, 4, 5] => left_depth == 2 and right_depth == 1
        #      in this case the right sub-tree is complete
        #
        # also dont' forget to add 1 in return value since we need to count root also
        nodes_num = 0
        curr_node = root
        while curr_node is not None:
            left_depth  = self.count_depth(curr_node.left)
            right_depth = self.count_depth(curr_node.right)

            if left_depth == right_depth:
                left_sub_tree_size = pow(2, left_depth) - 1
                nodes_num += 1 + left_sub_tree_size
                curr_node = curr_node.right
            else:
                right_sub_tree_size = pow(2, right_depth) - 1
                nodes_num += 1 + right_sub_tree_size
                curr_node = curr_node.left
        return nodes_num

    def count_depth(self, node):
        if node is None:
            return 0

        curr_depth = 1
        curr_node = node
        while curr_node.left is not None:
            curr_depth += 1
            curr_node = curr_node.left
        return curr_depth
