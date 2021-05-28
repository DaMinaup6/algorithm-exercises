# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.sort_list(head)

    def get_divided_heads(self, head: ListNode) -> List[ListNode]:
        prev = slow = fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        return [head, slow]

    def sort_list(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        left_head, right_head = self.get_divided_heads(head)
        left_head  = self.sort_list(left_head)
        right_head = self.sort_list(right_head)
        return self.merge_two_sorted_lists(left_head, right_head)

    def merge_two_sorted_lists(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        node_1 = head_1
        node_2 = head_2
        if head_1.val <= head_2.val:
            head = head_1
            node = head_1
            node_1 = head_1.next
        else:
            head = head_2
            node = head_2
            node_2 = head_2.next

        while node_1 is not None or node_2 is not None:
            if node_1 is None:
                node.next = node_2
                return head
            if node_2 is None:
                node.next = node_1
                return head

            if node_1.val <= node_2.val:
                node.next = node_1
                node_1 = node_1.next
                node = node.next
            else:
                node.next = node_2
                node_2 = node_2.next
                node = node.next

        return head
