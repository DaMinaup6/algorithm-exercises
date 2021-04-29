# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n * math.comb(2n, n) / (n + 1))
# Space Complexity: O(math.comb(2n, n) / (n + 1))
# -----------------------------------------
# Ref: https://en.wikipedia.org/wiki/Catalan_number
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(vals):
            if len(vals) == 0:
                return []
            if len(vals) == 1:
                return [TreeNode(vals[0])]
            
            nodes = []
            for index, val in enumerate(vals):
                left_nodes  = dfs(vals[:index])
                right_nodes = dfs(vals[(index + 1):])

                # Note: left_nodes and right_nodes should not be empty at same time here
                if len(left_nodes) == 0:
                    for right_node in right_nodes:
                        nodes.append(TreeNode(val, None, right_node))
                elif len(right_nodes) == 0:
                    for left_node in left_nodes:
                        nodes.append(TreeNode(val, left_node))
                else:
                    for left_node in left_nodes:
                        for right_node in right_nodes:
                            nodes.append(TreeNode(val, left_node, right_node))
            return nodes

        return dfs(list(range(1, n + 1)))
