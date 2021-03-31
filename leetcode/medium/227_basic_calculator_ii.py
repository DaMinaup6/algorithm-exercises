# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def calculate(self, s: str) -> int:
        operators_set = set(['+', '-', '*', '/'])

        tmp_num = None
        is_negative = False
        to_process = []
        for char in s:
            if char.isdigit():
                if tmp_num is None:
                    tmp_num = int(char)
                    if is_negative:
                        tmp_num *= -1
                else:
                    tmp_num *= 10
                    if is_negative:
                        tmp_num -= int(char)
                    else:
                        tmp_num += int(char)
            elif char in operators_set:
                is_negative = char == '-'
                if char == '*' or char == '/':
                    to_process.extend([tmp_num, char])
                elif tmp_num is not None:
                    to_process.append(tmp_num)
                tmp_num = None
        if tmp_num is not None:
            to_process.append(tmp_num)

        result = []
        cursor = 0
        while cursor < len(to_process):
            element = to_process[cursor]
            if element == '*' or element == '/':
                if element == '*':
                    result[-1] *= to_process[cursor + 1]
                else:
                    result[-1] = int(result[-1] / to_process[cursor + 1])
                cursor += 2
            else:
                result.append(element)
                cursor += 1

        return int(sum(result))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/80826333
class Solution:
    def calculate(self, s):
        prev_op = '+'
        tmp_num = 0
        val_num = 0
        ans_num = 0
        for index, char in enumerate(s):
            if char.isdigit():
                tmp_num = 10 * tmp_num + int(char)

            if char in '+-*/' or index == len(s) - 1:
                if prev_op == '+':
                    ans_num += val_num
                    val_num = tmp_num
                elif prev_op == '-':
                    ans_num += val_num
                    val_num = -tmp_num
                elif prev_op == '*':
                    val_num *= tmp_num
                elif prev_op == '/':
                    val_num = int(val_num / tmp_num)
                prev_op = char
                tmp_num = 0

        return ans_num + val_num

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/basic-calculator-ii/solution/771753
class Solution:
    def calculate(self, s: str) -> int:
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
