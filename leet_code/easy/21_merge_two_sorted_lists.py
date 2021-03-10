# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = None
        node = None
        node_1 = l1
        node_2 = l2
        while True:
            if node is None:
                if node_1.val <= node_2.val:
                    head = node_1
                    node_1 = node_1.next
                else:
                    head = node_2
                    node_2 = node_2.next

                node = head
            elif node_1 is None:
                node.next = node_2
                break
            elif node_2 is None:
                node.next = node_1
                break
            else:
                if node_1.val <= node_2.val:
                    node.next = node_1
                    node_1 = node_1.next
                else:
                    node.next = node_2
                    node_2 = node_2.next

                node = node.next

        return head
