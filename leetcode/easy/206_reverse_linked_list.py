# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        nodes = []
        node  = head
        while node is not None:
            nodes.append(node)
            node = node.next

        for index in range(len(nodes) - 1, 0, -1):
            nodes[index].next = nodes[index - 1]
        nodes[0].next = None

        return nodes[-1]

# -----------------------------------------
# Iteration
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# -----------------------------------------
# Recursion
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        reversed_head  = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_head
