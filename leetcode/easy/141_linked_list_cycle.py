# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
import sys

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        node = head
        while node.next is not None:
            if node.val == sys.maxsize:
                return True
            node.val = sys.maxsize
            node = node.next

        return False

# -----------------------------------------
# Floyd Cycle Detection (Two Pointers)
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
