# -----------------------------------------
# My Solution: Stack
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
 class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        stack = []
        for char in num:
            while len(stack) > 0 and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        while k > 0:
            stack.pop()
            k -= 1

        return str(int("".join(stack)))
