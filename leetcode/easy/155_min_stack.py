# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n) for pop, O(1) for others
# Space Complexity: O(n)
# -----------------------------------------
class MinStack:

    def __init__(self):
        self.stack   = []
        self.min_val = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_val = min(self.min_val, x)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if pop_val == self.min_val:
            self.min_val = min(self.stack) if len(self.stack) > 0 else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(n)
# -----------------------------------------
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack  = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        pop_val = self.main_stack.pop()
        if pop_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
