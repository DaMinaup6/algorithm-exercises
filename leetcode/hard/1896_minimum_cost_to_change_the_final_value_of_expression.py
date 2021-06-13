# -----------------------------------------
# Model Solution: Dynamic Programming + Stack
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/discuss/1267522/Python-DP-O(n)

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        # (original value, number of operations to flip the value of sub expression)
        def calculate_value_min_cost(sub_expression_1, operator, sub_expression_2):
            if operator == '&':
                if sub_expression_1[0] == 1 and sub_expression_2[0] == 1:
                    # just turn sub_expression_1 or sub_expression_2 into 0, need min(sub_expression_1[1], sub_expression_2[1])
                    return (1, min(sub_expression_1[1], sub_expression_2[1]))
                elif sub_expression_1[0] == 1 and sub_expression_2[0] == 0:
                    # just turn & into | so need only one move
                    return (0, 1)
                if sub_expression_1[0] == 0 and sub_expression_2[0] == 1:
                    # just turn & into | so need only one move
                    return (0, 1)
                if sub_expression_1[0] == 0 and sub_expression_2[0] == 0:
                    # a) turn sub_expression_1 into 1 and & -> |
                    # b) turn sub_expression_2 into 1 and & -> |
                    # c) turn sub_expression_1 into 1 and sub_expression_2 into 1
                    return (0, min(1 + sub_expression_1[1], 1 + sub_expression_2[1], sub_expression_1[1] + sub_expression_2[1]))
            elif operator == '|':
                if sub_expression_1[0] == 1 and sub_expression_2[0] == 1:
                    # a) turn sub_expression_1 into 0 and | -> &
                    # b) turn sub_expression_2 into 0 and | -> &
                    # c) turn sub_expression_1 into 0 and sub_expression_2 into 0
                    return (1, min(1 + sub_expression_1[1], 1 + sub_expression_2[1], sub_expression_1[1] + sub_expression_2[1]))
                elif sub_expression_1[0] == 1 and sub_expression_2[0] == 0:
                    # just turn | into & so need only one move
                    return (1, 1)
                if sub_expression_1[0] == 0 and sub_expression_2[0] == 1:
                    # just turn | into & so need only one move
                    return (1, 1)
                if sub_expression_1[0] == 0 and sub_expression_2[0] == 0:
                    # just turn sub_expression_1 or sub_expression_2 into 1, need min(sub_expression_1[1], sub_expression_2[1])
                    return (0, min(sub_expression_1[1], sub_expression_2[1]))

        # e.g. expression == "1&(0|1)"
        #      it's like we calculate "0|1" first since it's wrapped by brackets, so we get
        #      (1, 1), where first element represents eval("0|1") and second element represents how many
        #      operations needed to flip the original result
        #      in this case we need to change '|' into '&' to flip the value so second element is 1
        #
        #      then we check "1&1" (since we calculate ("0|1") first so we replace it by just 1)
        #      we already knew how many operations needed to flip the value of second element
        #      and to flip the value of first element only takes 1 operation (from "1" to "0" takes 1 operation)
        #      so we can get the final result
        stack = [[]]
        for char in expression:
            if char == '(':
                stack.append([])
            elif char == ')':
                prev_result = stack.pop()
                stack[-1].append(prev_result[-1])
            elif char == '0' or char == '1':
                stack[-1].append((int(char), 1))
            else:
                stack[-1].append(char)

            if len(stack[-1]) == 3:
                result = calculate_value_min_cost(stack[-1][0], stack[-1][1], stack[-1][2])
                stack[-1] = [result]

        return stack[-1][-1][1]
