class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = [head]
        node_cursor = 1
        current_node = head

        while current_node.next is not None:
            nodes.append(current_node.next)
            current_node = current_node.next
            node_cursor += 1

        target_index = node_cursor - n
        if target_index == 0:
            return nodes[1] if node_cursor > 1 else None
        else:
            nodes[target_index - 1].next = None if n == 1 else nodes[target_index + 1]
            return head

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        # condition n <= list_size specified in the description, so if fast is None then the only possible case is n == list_size
        if fast is None:
            return head.next

        prev = None
        while fast is not None:
            fast = fast.next
            if fast is None:
                prev = slow
            slow = slow.next
        prev.next = slow.next

        return head
