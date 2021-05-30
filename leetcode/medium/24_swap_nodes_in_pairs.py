# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head  = head.next
        head.next = new_head.next
        new_head.next = head

        prev_node = new_head.next
        curr_node = new_head.next.next
        while curr_node is not None and curr_node.next is not None:
            next_node = curr_node.next
            # prev_node -> curr_node -> next_node -> next_node.next => prev_node -> next_node -> curr_node -> next_node.next
            curr_node.next = next_node.next
            prev_node.next = next_node
            next_node.next = curr_node

            prev_node = prev_node.next.next
            curr_node = curr_node.next

        return new_head
