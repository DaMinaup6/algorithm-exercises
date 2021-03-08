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

        self.head.prev = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if self.hash.get(key) is None:
            return -1

        node = self.hash[key]
        self.__isolate_node(node)
        self.__insert_node_to_first(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if self.size == self.capacity:
                self.__remove_last_node()
            self.__add_new_node(key, value)
        else:
            self.hash[key].value = value

    def __isolate_node(self, node: Node) -> None:
        # (... - prev_node - node - next_node - ...) -> (... - prev_node - next_node - ...)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def __insert_node_to_first(self, node: Node) -> None:
        # insert node between first_node and self.head
        # (... - first_node - self.head) -> (... - first_node - node - self.head)
        first_node = self.head.prev
        first_node.next = node
        self.head.prev  = node
        node.prev = first_node
        node.next = self.head

    def __remove_last_node(self) -> None:
        # remove last_node between self.tail and next_node
        # (self.tail - last_node - next_node - ...) -> (self.tail - next_node - ...)
        last_node = self.tail.next
        next_node = last_node.next

        self.tail.next = next_node
        next_node.prev = self.tail

        del self.hash[last_node.key]
        del last_node
        self.size -= 1

    def __add_new_node(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        self.__insert_node_to_first(new_node)
        self.hash[new_node.key] = new_node
        self.size += 1
