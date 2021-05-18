# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(dominoes)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) == 0:
            return ""

        to_right_force = ["."] * len(dominoes)
        cursor = 0
        while cursor < len(dominoes):
            if dominoes[cursor] == "R":
                while cursor < len(dominoes) and dominoes[cursor] != "L":
                    to_right_force[cursor] = "R"
                    cursor += 1
            else:
                cursor += 1

        to_left_force = ["."] * len(dominoes)
        cursor = len(dominoes) - 1
        while cursor >= 0:
            if dominoes[cursor] == "L":
                while cursor >= 0 and dominoes[cursor] != "R":
                    to_left_force[cursor] = "L"
                    cursor -= 1
            else:
                cursor -= 1

        output = ["."] * len(dominoes)
        cursor = 0
        while cursor < len(dominoes):
            if to_right_force[cursor] == "R" and to_left_force[cursor] == ".":
                output[cursor] = "R"
                cursor += 1
            elif to_right_force[cursor] == "." and to_left_force[cursor] == "L":
                output[cursor] = "L"
                cursor += 1
            elif to_right_force[cursor] == "R" and to_left_force[cursor] == "L":
                end_cursor = cursor
                while end_cursor + 1 < len(dominoes) and to_right_force[end_cursor + 1] == "R":
                    end_cursor += 1

                middle_cursor = (cursor + end_cursor) // 2
                # e.g.
                # "R..L"  -> "RRLL"
                # "R...L" -> "RR.LL"
                for index in range(cursor, middle_cursor + (1 if (end_cursor - cursor) % 2 == 1 else 0)):
                    output[index] = "R"
                for index in range(middle_cursor + 1, end_cursor + 1):
                    output[index] = "L"
                cursor = end_cursor + 1
            else:
                cursor += 1
        return "".join(output)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(dominoes)
# Ref: https://leetcode.com/problems/push-dominoes/solution/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        curr_force = 0
        for index in range(n):
            if dominoes[index] == "R":
                curr_force = n
            elif dominoes[index] == "L":
                curr_force = 0
            else:
                curr_force = max(curr_force - 1, 0)
            forces[index] += curr_force

        curr_force = 0
        for index in range(n - 1, -1, -1):
            if dominoes[index] == "R":
                curr_force = 0
            elif dominoes[index] == "L":
                curr_force = -n
            else:
                curr_force = min(curr_force + 1, 0)
            forces[index] += curr_force

        return "".join("." if force == 0 else ("R" if force > 0 else "L") for force in forces)
