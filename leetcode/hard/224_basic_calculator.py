# -----------------------------------------
# Model Solution: Stack
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/basic-calculator/discuss/62418/Python-with-stack
class Solution:
    def calculate(self, s: str) -> int:
        # stack stores sign for parentheses
        # e.g. s == "3-(4-5)"
        # it equals "3-4+5", so when we met "(", we append -1 to stack, so when we encounter "-" in "4-5", we will add 4 * 1 * -1 to ans
        ans, num, sign, stack = 0, 0, 1, [1]
        for char in s + "+": # Add "+" sign at the end to force add last number to ans
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in "+-":
                ans += num * sign * stack[-1]
                sign = 1 if char == "+" else -1
                num = 0
            elif char == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif char == ")":
                ans += num * sign * stack[-1]
                num = 0
                stack.pop()
        return ans
