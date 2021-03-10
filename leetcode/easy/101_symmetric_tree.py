# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution: BFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
def arr_symmetric(arr):
    for index in range(len(arr) // 2):
        if arr[index] != arr[len(arr) - 1 - index]:
            return False

    return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True

        nodes = []
        nodes.append(root.left  if root.left  is not None else None)
        nodes.append(root.right if root.right is not None else None)

        while len(nodes) > 0:
            values, children = [], []
            has_child = False

            for node in nodes:
                if node is not None:
                    values.append(node.val)

                    if node.left is not None:
                        children.append(node.left)
                        has_child = True
                    else:
                        children.append(None)

                    if node.right is not None:
                        children.append(node.right)
                        has_child = True
                    else:
                        children.append(None)
                else:
                    values.append(None)
                    children += [None, None]

            if not arr_symmetric(values):
                return False

            nodes = children if has_child else []

        return True

# -----------------------------------------
# BFS (simplified)
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        nodes = [root.left, root.right]
        while len(nodes) > 0:
            node_1 = nodes.pop()
            node_2 = nodes.pop()

            if node_1 is None and node_2 is None:
                continue
            if node_1 is None or node_2 is None or node_1.val != node_2.val:
                return False

            nodes.append(node_1.right)
            nodes.append(node_2.left)
            nodes.append(node_1.left)
            nodes.append(node_2.right)

        return True

# -----------------------------------------
# Recursive
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def is_mirror(node_1, node_2):
        if node_1 is None and node_2 is None:
            return True
        if node_1 is None or node_2 is None:
            return False

        return node_1.val == node_2.val and self.is_mirror(node_1.left, node_2.right) and self.is_mirror(node_1.right, node_2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
