# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_L_indexes, end_L_indexes = [], []
        start_R_indexes, end_R_indexes = [], []
        for index in range(len(start)):
            if start[index] == "L":
                start_L_indexes.append(index)
            if start[index] == "R":
                start_R_indexes.append(index)
            if end[index] == "L":
                end_L_indexes.append(index)
            if end[index] == "R":
                end_R_indexes.append(index)

        if len(start_L_indexes) != len(end_L_indexes) or len(start_R_indexes) != len(end_R_indexes):
            return False

        start, end = [char for char in start], [char for char in end]

        for idx, start_L_index in enumerate(start_L_indexes):
            if start_L_index < end_L_indexes[idx]:
                return False
            while start_L_index != end_L_indexes[idx]:
                if start[start_L_index - 1] != "X":
                    return False
                start[start_L_index], start[start_L_index - 1] = start[start_L_index - 1], start[start_L_index]
                start_L_index -= 1
            start_L_indexes[idx] = start_L_index

        for idx in range(len(start_R_indexes) - 1, -1, -1):
            start_R_index = start_R_indexes[idx]
            if start_R_index > end_R_indexes[idx]:
                return False
            while start_R_index != end_R_indexes[idx]:
                if start[start_R_index + 1] != "X":
                    return False
                start[start_R_index], start[start_R_index + 1] = start[start_R_index + 1], start[start_R_index]
                start_R_index += 1
            start_R_indexes[idx] = start_R_index

        return True

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/217070/Python-using-corresponding-position-
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_LR_indexes = [(char, index) for index, char in enumerate(start) if char in "LR"]
        end_LR_indexes = [(char, index) for index, char in enumerate(end) if char in "LR"]
        if len(start_LR_indexes) != len(end_LR_indexes):
            return False

        # the key point here is that order of char in start_LR_indexes and end_LR_indexes should be the same, otherwise False
        for compare_index in range(len(start_LR_indexes)):
            start_char, start_index = start_LR_indexes[compare_index]
            end_char, end_index = end_LR_indexes[compare_index]
            if start_char != end_char:
                return False
            elif start_char == "L" and start_index < end_index:
                return False
            elif start_char == "R" and start_index > end_index:
                return False
        return True
