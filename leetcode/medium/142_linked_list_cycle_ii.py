# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None

# -----------------------------------------
# Floyd Cycle Detection (Two Pointers)
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def get_cycle_node(self, head):
        if head is None:
            return None

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

    def detectCycle(self, head: ListNode) -> ListNode:
        cycle_node = self.get_cycle_node(head)
        if cycle_node is None:
            return None

        node = head
        while node != cycle_node:
            node = node.next
            cycle_node = cycle_node.next

        return node
