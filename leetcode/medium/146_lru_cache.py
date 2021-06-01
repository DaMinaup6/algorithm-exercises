# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dict = {}
#
#     def get(self, key: int) -> int:
#         if self.dict.get(key) is not None:
#             value = self.dict[key]
#             self.dict.pop(key)
#             self.dict[key] = value
#
#             return value
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if self.get(key) != -1:
#             self.dict[key] = value
#         else:
#             if len(self.dict.keys()) >= self.capacity:
#                 key_to_pop = list(self.dict.keys())[0]
#                 self.dict.pop(key_to_pop)
#
#             self.dict[key] = value

# -----------------------------------------
# Doubly Linked List
#
# Time  Complexity: O(1)
# Space Complexity: O(n)
# -----------------------------------------
class Node:

    def __init__(self, key: int, value: int):
        self.key   = key
        self.value = value
        self.prev  = None
        self.next  = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.hash = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.hash.get(key) is None:
            return -1

        node = self.hash[key]
        self.insert_node_to_first(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if self.size == self.capacity:
                self.remove_last_node()
            self.size += 1

            new_node = Node(key, value)
            self.insert_node_to_first(new_node)
        else:
            # The node called already updated by self.get so no need self.insert_node_to_first here
            self.hash[key].value = value

    def insert_node_to_first(self, node: Node) -> None:
        # head <-> first_node <-> ... <-> prev_node <-> node <-> next_node <-> ... => head <-> node <-> first_node <-> ... <-> prev_node <-> next_node <-> ...
        if node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next      = node

        self.hash[node.key] = node

    def remove_last_node(self) -> None:
        # head <-> ... <-> prev_node <-> last_node <-> tail => head <-> ... <-> prev_node <-> tail
        last_node = self.tail.prev
        last_node.prev.next = self.tail
        last_node.next.prev = last_node.prev

        del self.hash[last_node.key]
        del last_node
        self.size -= 1
