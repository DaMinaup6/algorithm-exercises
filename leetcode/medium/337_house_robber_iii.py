# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# Model Solution: Recursion
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/house-robber-iii/solution/
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)

            left  = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)

            return [rob, not_rob]

        return max(helper(root))

# -----------------------------------------
# Model Solution: Recursion with Memoization
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/house-robber-iii/solution/
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)

# -----------------------------------------
# Model Solution: Recursion with Memoization (simplified by lru_cache)
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=mSzz_bZUVCQ
from functools import lru_cache

class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def helper(node, parent_robbed):
            if node is None:
                return 0

            if parent_robbed:
                # got only one option here, not rob node
                return helper(node.left, False) + helper(node.right, False)
            else:
                # two options: 1) rob node 2) not rob node
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_robbed = helper(node.left, False) + helper(node.right, False)

                return max(rob, not_robbed)

        return helper(root, False)

# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/house-robber-iii/solution/
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        # reform tree into array-based tree
        tree  = []
        graph = {-1: []}
        index = -1
        queue = [(root, -1)]
        while queue:
            node, parent_index = queue.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                queue.append((node.left,  index))
                queue.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index + 1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index + 1)

        for i in range(index, -1, -1):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child] for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child]) for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])
