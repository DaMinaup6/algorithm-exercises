# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/basic-calculator-ii/solution/771753
class Solution:
    def calculate(self, s: str) -> int:
        no_parentheses_s = ''

        s_cursor = 0
        while s_cursor < len(s):
            if s[s_cursor] == '(':
                s_cursor += 1

                tmp_s = ['']
                while s_cursor < len(s) and len(tmp_s) > 0:
                    if s[s_cursor] == '(':
                        tmp_s.append('')
                    elif s[s_cursor] == ')':
                        tmp_no_parentheses_s = str(self.no_parentheses_calculate(tmp_s.pop()))
                        if len(tmp_s) > 0:
                            tmp_s[-1] += tmp_no_parentheses_s
                        else:
                            no_parentheses_s += tmp_no_parentheses_s
                    else:
                        tmp_s[-1] += s[s_cursor]

                    s_cursor += 1
            else:
                no_parentheses_s += s[s_cursor]
                s_cursor += 1

        return self.no_parentheses_calculate(no_parentheses_s)

    def no_parentheses_calculate(self, s: str) -> int:
        inner, outer, result, prev_operator = 0, 0, 0, '+'
        for char in s + '+':
            if char == ' ':
                continue
            if char.isdigit():
                inner = 10 * inner + int(char)
                continue

            if prev_operator == '+':
                result += outer
                outer = inner
            elif prev_operator == '-':
                result += outer
                outer = -inner
            elif prev_operator == '*':
                outer *= inner
            elif prev_operator == '/':
                outer = int(outer / inner)
            inner, prev_operator = 0, char

        return result + outer

processor = Solution()
print(processor.calculate("1 + 1") == 2)
print(processor.calculate("(1 + 1)") == 2)
print(processor.calculate("((1 + 2) * 3)") == 9)
print(processor.calculate(" 6-4 / 2 ") == 4)
print(processor.calculate("2*(5+5*2)/3+(6/2+8)") == 21)
print(processor.calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12)
