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
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        vals = []
        if root is None:
            return []
        else:
            vals.append(root.val)

        nodes = []
        if root.left:
            nodes.append(root.left)
        if root.right:
            nodes.append(root.right)
        while len(nodes) > 0:
            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            vals.append(nodes[-1].val)
            nodes = next_nodes

        return vals
