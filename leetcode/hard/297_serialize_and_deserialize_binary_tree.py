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
        def pre_order_traversal(root):
            if root is None:
                vals.append('None')
            else:
                vals.append(str(root.val))
                pre_order_traversal(root.left)
                pre_order_traversal(root.right)
        pre_order_traversal(root)
        return ",".join(vals)

    def deserialize(self, data):
        # e.g. root == [1, 2, 3, null, null, 4, 5]
        #      here vals == deque(['1', '2', 'None', 'None', '3', '4', 'None', 'None', '5', 'None', 'None'])
        #      the key is that we always append 'None' after node value if it has no left or right child node
        vals = deque(val for val in data.split(","))
        def build():
            if len(vals) > 0:
                val = vals.popleft()
                if val == 'None':
                    return None

                root = TreeNode(int(val))
                root.left  = build()
                root.right = build()
                return root
        return build()
