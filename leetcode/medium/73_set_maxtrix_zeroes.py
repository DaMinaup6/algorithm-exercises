# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.spread_tmp_values_from(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'zero':
                    matrix[i][j] = 0

    def spread_tmp_values_from(self, matrix: List[List[int]], i: int, j: int) -> None:
        for sub_i in range(len(matrix)):
            for sub_j in range(len(matrix[0])):
                if (sub_i == i or sub_j == j) and matrix[sub_i][sub_j] != 0:
                    matrix[sub_i][sub_j] = 'zero'

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution(object):
    def setZeroes(self, matrix):
        need_update_first_col = False
        for i in range(len(matrix)):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                need_update_first_col = True
            for j in range(1, len(matrix[0])):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if need_update_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
