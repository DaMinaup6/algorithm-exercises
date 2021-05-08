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
import collections

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums = collections.deque()

        nodes = [root]
        while len(nodes) > 0:
            curr_node = nodes[-1]
            if curr_node.left is not None:
                nodes.append(curr_node.left)
                curr_node.left = None
            else:
                nodes.pop()
                self.nums.append(curr_node.val)
                if curr_node.right is not None:
                    nodes.append(curr_node.right)
                    curr_node.right = None


    def next(self) -> int:
        return self.nums.popleft()


    def hasNext(self) -> bool:
        return len(self.nums) > 0
