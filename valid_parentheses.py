class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        tmp_s = ''
        for char in s:
            if char == '(' or char == '[' or char == '{':
                tmp_s += char
            elif len(tmp_s) == 0:
                return False
            elif char == ')' and tmp_s[-1] != '(' or char == ']' and tmp_s[-1] != '[' or char == '}' and tmp_s[-1] != '{':
                return False
            else:
                tmp_s = tmp_s[:-1]

        return len(tmp_s) == 0
