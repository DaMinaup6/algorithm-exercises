# in priority queue pq, for node with index i, its left child is with index 2i, right child with index 2i + 1
# therefore we should define pq[0] as None since index 0 doesn't obey the rule
class maxPriorityQueue:
    # implement a maximum priority queue by binary heap
    def __init__(self, array=[]):
        self.heap = [None]  # None for the array[0]
        self.length = 0

        if len(array) != 0:
            for item in array:
                self.insert(item)

    def insert(self, item):
        # insert item to the end then swim it up
        self.heap.append(item)
        self.length = self.length + 1
        self.__swim(self.length)

    def find(self, item, start_index=1):
        if self.heap[start_index] == item:
            return start_index
        else:
            if 2 * start_index <= self.length:
                item_index = self.find(item, 2 * start_index)
                if item_index != -1:
                    return item_index

            if 2 * start_index + 1 <= self.length:
                item_index = self.find(item, 2 * start_index + 1)
                if item_index != -1:
                    return item_index

        return -1

    def extract_max(self):
        # exchange first item and last item, then order again
        maximum = self.heap[1]
        self.__remove(1)

        return maximum

    def remove(self, item):
        item_index = self.find(item)
        if item_index != -1:
            self.__remove(item_index)

    def __swim(self, k):
        # Exchange key in child with key in parent. Repeat until heap order restored.
        while k > 1 and self.__less(k // 2, k):
            self.__exchange(k // 2, k)
            k //= 2

    def __sink(self, node_idx):
        # Key in parent exchange with ket in larger child. Repeat until heap order restored.
        while node_idx * 2 <= self.length:
            left_child_idx  = node_idx * 2
            right_child_idx = left_child_idx + 1 if left_child_idx < self.length else -1

            if self.__less(left_child_idx, node_idx) and (right_child_idx == -1 or self.__less(right_child_idx, node_idx)):
                break

            exchange_child_idx = right_child_idx if self.__less(left_child_idx, right_child_idx) else left_child_idx
            self.__exchange(node_idx, exchange_child_idx)
            node_idx = exchange_child_idx

    def __remove(self, item_index):
        self.__exchange(item_index, self.length)
        self.heap.pop()
        self.length = self.length - 1
        self.__sink(item_index)

    def __less(self, a, b):
        # return a boolean represent if item at a position is less than item at b
        return self.heap[a] < self.heap[b]

    def __exchange(self, a, b):
        # swap item in the heap at position a and b
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

pq = maxPriorityQueue()
pq.insert(1)
pq.insert(3)
pq.insert(5)
pq.insert(2)
pq.insert(6)
pq.insert(9)
print(f"pq.heap after insert:      {pq.heap}")
print(f"pq.find(5) result index:   {pq.find(5)}")
pq.extract_max()
print(f"pq.heap after extract_max: {pq.heap}")
pq.remove(5)
print(f"pq.heap after remove(5):   {pq.heap}")
