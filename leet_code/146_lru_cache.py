# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if self.dict.get(key) is not None:
            value = self.dict[key]
            self.dict.pop(key)
            self.dict[key] = value

            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.dict[key] = value
        else:
            if len(self.dict.keys()) >= self.capacity:
                key_to_pop = list(self.dict.keys())[0]
                self.dict.pop(key_to_pop)

            self.dict[key] = value
