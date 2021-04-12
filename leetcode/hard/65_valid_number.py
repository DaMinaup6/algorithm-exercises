# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(s)
class Solution:
    def isNumber(self, s: str) -> bool:
        for index, char in enumerate(s):
            if char in 'eE':
                return self.is_decimal(s[:index]) and self.is_integer(s[(index + 1):])
        
        return self.is_decimal(s)

    def is_decimal(self, s: str) -> bool:
        if len(s) <= 1:
            return s.isdigit()
        if s[0] in '+-':
            s = s[1:]
        if any(char != '.' and not char.isdigit() for char in s):
            return False

        for index, char in enumerate(s):
            if char == '.':
                if index == 0:
                    return self.is_integer(s[1:])
                if index == len(s) - 1:
                    return self.is_integer(s[:-1])
                return self.is_integer(s[:index]) and self.is_integer(s[(index + 1):])

        return self.is_integer(s)

    def is_integer(self, s: str) -> bool:
        if len(s) <= 1:
            return s.isdigit()
        if s[0] in '+-':
            s = s[1:]

        return all(char.isdigit() for char in s)
