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
from collections import deque

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None

        nodes = deque()
        curr_node = head.next
        while curr_node is not None:
            nodes.append(curr_node)
            curr_node = curr_node.next

        curr_node = head
        curr_pop  = 1
        while len(nodes) > 0:
            if curr_pop == 1:
                curr_node.next = nodes.pop()
            else:
                curr_node.next = nodes.popleft()
            curr_node = curr_node.next
            curr_pop *= -1
            if len(nodes) == 0:
                curr_node.next = None

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/80805434
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None or head.next.next is None:
            return None

        # find mid node of original list, which is the end node of reordered list
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head_1 = head
        head_2 = slow.next
        slow.next = None

        # reverse linked list head_2
        # head_2 -> node_2_1 -> node_2_2 -> ... -> tail_2
        # change node.next step by step. e.g. dummy -> head_2 => dummy -> node_2_1 -> head_2 => dummy -> node_2_2 -> node_2_1 -> head_2 ...
        dummy = ListNode(0)
        dummy.next  = head_2
        curr_node_2 = head_2.next
        head_2.next = None
        while curr_node_2 is not None:
            temp = curr_node_2
            curr_node_2 = curr_node_2.next
            temp.next   = dummy.next
            dummy.next  = temp
        head_2 = dummy.next

        # merge two linked list head_1 and head_2
        curr_node_1 = head_1
        curr_node_2 = head_2
        while curr_node_2:
            temp1 = curr_node_1.next
            temp2 = curr_node_2.next
            curr_node_1.next = curr_node_2
            curr_node_2.next = temp1
            curr_node_1 = temp1
            curr_node_2 = temp2
