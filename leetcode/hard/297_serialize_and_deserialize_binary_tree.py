# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

# -----------------------------------------
# Model Solution: Preorder
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79571892
from collections import deque

class Codec:

    def serialize(self, root):
        vals = []
        def preOrder(root):
            if not root:
                vals.append('None')
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = deque(val for val in data.split(','))
        def build():
            if vals:
                val = vals.popleft()
                if val == 'None':
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root
        return build()
