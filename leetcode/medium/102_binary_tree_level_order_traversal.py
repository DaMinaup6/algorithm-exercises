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
    def levelOrder(self, root):
        if root is None:
            return []

        orders = [[root.val]]
        nodes  = self.__left_right_child_of(root)
        while len(nodes) > 0:
            order = []
            children = []

            for node in nodes:
                order.append(node.val)
                children += self.__left_right_child_of(node)

            orders.append(order)
            nodes = children

        return orders

    def __left_right_child_of(self, node):
        children = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)

        return children
