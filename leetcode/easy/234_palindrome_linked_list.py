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
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []

        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        
        for i in range(len(vals) // 2):
            if vals[i] != vals[len(vals) - 1 - i]:
                return False
        
        return True

# -----------------------------------------
# Reverse List + Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/coder_orz/article/details/51306985
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        # find the middle node (which would be slow after while loop)
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        slow = self.reverse_list(slow)
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next

        return True

    def reverse_list(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node

        return prev_node
