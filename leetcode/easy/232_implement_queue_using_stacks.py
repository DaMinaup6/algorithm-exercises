# -----------------------------------------
# Model Solution
#
# Time  Complexity: Amortized O(1)
# Space Complexity: O(n)
# -----------------------------------------
class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []


    def push(self, x: int) -> None:
        self.stack_1.append(x)


    def pop(self) -> int:
        if len(self.stack_2) == 0:
            self.peek()
        return self.stack_2.pop()


    def peek(self) -> int:
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]


    def empty(self) -> bool:
        return len(self.stack_1) == 0 and len(self.stack_2) == 0
