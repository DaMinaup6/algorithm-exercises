# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        paths_num = 0
        def dfs(node):
            nonlocal paths_num
            if node is None:
                return

            paths_num += self.calc_paths_num_starts_at(node, target)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return paths_num

    def calc_paths_num_starts_at(self, node, target):
        if node is None:
            return 0

        paths_num = 0
        def dfs(current_node, current_sum):
            nonlocal paths_num
            if current_node is None:
                return
            if current_sum + current_node.val == target:
                paths_num += 1

            dfs(current_node.left,  current_sum + current_node.val)
            dfs(current_node.right, current_sum + current_node.val)

        dfs(node, 0)
        return paths_num

# -----------------------------------------
# Model Solution: DFS + DFS
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/71097135
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0

        return self.paths_num_from(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)

    def paths_num_from(self, node, target):
        if node is None:
            return 0

        paths_num = 0
        target -= node.val
        if target == 0:
            paths_num += 1

        paths_num += self.paths_num_from(node.left,  target)
        paths_num += self.paths_num_from(node.right, target)
        return paths_num

# -----------------------------------------
# Model Solution: DFS + Memoization
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://maxming0.github.io/2020/08/08/Path-Sum-III/
# b) https://youtu.be/ofMqFAFVcKY?t=214
# c) https://www.youtube.com/watch?v=6jYxwdwjwKg
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        paths_num  = 0
        prefix_sum = {0: 1}
        def dfs(node, current_sum):
            nonlocal paths_num

            if not node:
                return

            # e.g. target == 8 and current_sum == 18
            # if now we got 10 in sum_dict, which means there are paths with sum 10 previously
            # so now we have paths with path sum 8
            current_sum += node.val
            paths_num   += prefix_sum.get(current_sum - target, 0) # if use defaultdict then we may increase prefix_sum size with many redudant current_sum - target keys

            prefix_sum[current_sum]  = prefix_sum.get(current_sum, 0) + 1
            dfs(node.left,  current_sum)
            dfs(node.right, current_sum)
            prefix_sum[current_sum] -= 1 # remove current_sum from prefix_sum after dfs to avoid wrong calculation in other branches

        dfs(root, 0)
        return paths_num
