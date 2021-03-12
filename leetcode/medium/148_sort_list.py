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
        if head is None:
            return None

        list_len = self.get_list_len(head)
        return self.sort_list(head, list_len)

    def get_list_len(self, node: ListNode) -> ListNode:
        list_len = 0
        while node is not None:
            list_len += 1
            node = node.next

        return list_len

    def get_divided_heads(self, head: ListNode, divided_len: int) -> List[ListNode]:
        heads = [head]

        node = head
        node_index = 0
        while node_index < divided_len:
            if node_index == divided_len - 1:
                tmp_node = node.next
                node.next = None # need to remove connection between separated nodes
                node = tmp_node
                break
            else:
                node = node.next
                node_index += 1

        heads.append(node)
        return heads

    def sort_list(self, head: ListNode, list_len: int) -> ListNode:
        if list_len == 1:
            return head

        left_head, right_head = self.get_divided_heads(head, list_len // 2)
        left_head  = self.sort_list(left_head, list_len // 2)
        right_head = self.sort_list(right_head, list_len - list_len // 2)

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
