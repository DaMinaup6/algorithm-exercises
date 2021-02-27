def merge_two_lists(l1, l2):
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

def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return merge_two_lists(lists[0], lists[1])

    mid = len(lists) // 2
    return merge_two_lists(merge_k_lists(lists[:mid]), merge_k_lists(lists[mid:]))
