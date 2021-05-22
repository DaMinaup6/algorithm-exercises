# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := number of nodes
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        position_num_arr = []
        def dfs(node, curr_row, curr_col):
            if node is None:
                return
            position_num_arr.append((curr_col, curr_row, node.val))
            dfs(node.left,  curr_row + 1, curr_col - 1)
            dfs(node.right, curr_row + 1, curr_col + 1)
        dfs(root, 0, 0)
        position_num_arr.sort()

        output = []
        curr_col = position_num_arr[0][0]
        curr_arr = [position_num_arr[0][2]]
        for index in range(1, len(position_num_arr)):
            if position_num_arr[index][0] == curr_col:
                curr_arr.append(position_num_arr[index][2])
            else:
                output.append(curr_arr)
                curr_col = position_num_arr[index][0]
                curr_arr = [position_num_arr[index][2]]
        output.append(curr_arr)
        return output
