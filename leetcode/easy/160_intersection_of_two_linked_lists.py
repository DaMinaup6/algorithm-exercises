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
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        lenA = self.get_list_len(headA)
        lenB = self.get_list_len(headB)

        node_A = headA
        node_B = headB
        if lenA > lenB:
            cursor = 0
            while cursor < lenA - lenB:
                node_A = node_A.next
                cursor += 1
        elif lenA < lenB:
            cursor = 0
            while cursor < lenB - lenA:
                node_B = node_B.next
                cursor += 1

        cursor = 0
        while cursor < min(lenA, lenB):
            if node_A == node_B:
                return node_A
            node_A = node_A.next
            node_B = node_B.next
            cursor += 1

        return None

    def get_list_len(self, head: ListNode) -> int:
        list_len = 0

        node = head
        while node is not None:
            list_len += 1
            node = node.next

        return list_len

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        node_A = headA
        node_B = headB
        while node_A != node_B:
            node_A = node_A.next if node_A is not None else headB
            node_B = node_B.next if node_B is not None else headA

        return node_A
