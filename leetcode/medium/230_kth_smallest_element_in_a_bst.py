# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: average - O(n), worst - O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        left_size = self.node_num(root.left)
        if left_size == k - 1:
            return root.val
        elif left_size > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_size)

    def node_num(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            num = 1
            num += self.node_num(root.left)
            num += self.node_num(root.right)

        return num

# -----------------------------------------
# My Solution: Inorder Traversal
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums_count = 0
        target_num = 0
        def find_target_num(node):
            nonlocal nums_count, target_num

            if node is None or nums_count == k:
                return
            find_target_num(node.left)
            if nums_count < k:
                target_num  = node.val
                nums_count += 1
            find_target_num(node.right)

        find_target_num(root)
        return target_num

# -----------------------------------------
# Follow up: add size to each node
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class MyTreeNode:
    def __init__(self, val=0, left=None, right=None, size=1):
        self.val   = val
        self.left  = left
        self.right = right
        self.size  = size

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        my_root = self.construct_my_tree(root)
        return self.kth_smallest(my_root, k)

    def kth_smallest(self, root: MyTreeNode, k: int) -> int:
        left_size = root.left.size if root.left is not None else 0
        if left_size == k - 1:
            return root.val
        elif left_size > k - 1:
            return self.kth_smallest(root.left, k)
        else:
            return self.kth_smallest(root.right, k - 1 - left_size)

    def construct_my_tree(self, root: TreeNode) -> MyTreeNode:
        if root is None:
            return None

        my_root = MyTreeNode(root.val)
        my_root.left  = self.construct_my_tree(root.left)
        my_root.right = self.construct_my_tree(root.right)
        if my_root.left:
            my_root.size += my_root.left.size
        if my_root.right:
            my_root.size += my_root.right.size

        return my_root
