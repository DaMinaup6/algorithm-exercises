# -----------------------------------------
# My Solution
#
# Time  Complexity: O((m + n) * log(mn))
# Space Complexity: O(1)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search_matrix(matrix, target, 0, 0)

    def search_matrix(self, matrix: List[List[int]], target: int, i: int, j: int) -> bool:
        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
            return False
        if target == matrix[i][j]:
            return True
        if target < matrix[i][j]:
            return False

        next_row_val = matrix[i + 1][j] if i < len(matrix) - 1 else float('inf')
        next_col_val = matrix[i][j + 1] if j < len(matrix[0]) - 1 else float('inf')
        if target == next_row_val or target == next_col_val:
            return True
        if target < next_row_val and target < next_col_val:
            return False

        next_i = self.next_row_landing(matrix, target, j, i, len(matrix) - 1)
        next_j = self.next_col_landing(matrix, target, i, j, len(matrix[0]) - 1)
        if next_i > i and next_j > j:
            return self.search_matrix(matrix, target, next_i, j) or self.search_matrix(matrix, target, i, next_j) or self.search_matrix(matrix, target, i + 1, j + 1)
        elif next_i > i:
            return self.search_matrix(matrix, target, next_i, j)
        elif next_j > j:
            return self.search_matrix(matrix, target, i, next_j)

        return False

    def next_row_landing(self, matrix: List[List[int]], target: int, j: int, start_i: int, end_i: int) -> int:
        if start_i == end_i:
            return end_i

        middle_num = matrix[(start_i + end_i) // 2][j]
        if target == middle_num:
            return (start_i + end_i) // 2
        elif target > middle_num:
            if (start_i + end_i) // 2 < len(matrix) - 1 and target < matrix[(start_i + end_i) // 2 + 1][j]:
                return (start_i + end_i) // 2
            elif (start_i + end_i) // 2 < len(matrix) - 1 and target == matrix[(start_i + end_i) // 2 + 1][j]:
                return (start_i + end_i) // 2 + 1

            return self.next_row_landing(matrix, target, j, (start_i + end_i) // 2 + 1, end_i)
        else:
            if (start_i + end_i) // 2 > 0 and target >= matrix[(start_i + end_i) // 2 - 1][j]:
                return (start_i + end_i) // 2 - 1

            return self.next_row_landing(matrix, target, j, start_i, (start_i + end_i) // 2)

    def next_col_landing(self, matrix: List[List[int]], target: int, i: int, start_j: int, end_j: int) -> int:
        if start_j == end_j:
            return end_j

        middle_num = matrix[i][(start_j + end_j) // 2]
        if target == middle_num:
            return (start_j + end_j) // 2
        elif target > middle_num:
            if (start_j + end_j) // 2 < len(matrix[0]) - 1 and target < matrix[i][(start_j + end_j) // 2 + 1]:
                return (start_j + end_j) // 2
            elif (start_j + end_j) // 2 < len(matrix[0]) - 1 and target == matrix[i][(start_j + end_j) // 2 + 1]:
                return (start_j + end_j) // 2 + 1

            return self.next_col_landing(matrix, target, i, (start_j + end_j) // 2 + 1, end_j)
        else:
            if (start_j + end_j) // 2 > 0 and target >= matrix[i][(start_j + end_j) // 2 - 1]:
                return (start_j + end_j) // 2 - 1

            return self.next_col_landing(matrix, target, i, start_j, (start_j + end_j) // 2)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79459314
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        col_num = len(matrix[0])

        i, j = 0, col_num - 1
        while i < row_num and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False
