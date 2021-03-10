class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
