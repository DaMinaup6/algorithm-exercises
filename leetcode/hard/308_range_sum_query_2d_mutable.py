# -----------------------------------------
# Model Solution: Binary indexes Tree
#
# Space Complexity: O(mn)
# -----------------------------------------
# Ref:
# a) https://www.cnblogs.com/grandyang/p/5300458.html
# b) https://github.com/GJzh/Leetcode/blob/master/python/308%20Range%20Sum%20Query%202D%20-%20Mutable.py
class NumMatrix:

    # -----> Time Complexity: O(mn)
    def __init__(self, matrix):
        self.matrix = matrix
        self.bit_2d = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.update_tree_val(row, col, matrix[row][col])

    # -----> Time Complexity: O(log(m) * log(n))
    def update_tree_val(self, row, col, diff):
        row_index = row + 1
        while row_index <= len(self.matrix):
            col_index = col + 1
            while col_index <= len(self.matrix[0]):
                self.bit_2d[row_index][col_index] += diff
                col_index += col_index & (-col_index)
            row_index += row_index & (-row_index)

    # -----> Time Complexity: O(log(m) * log(n))
    def get_sum(self, row, col):
        region_sum = 0

        row_index = row + 1
        while row_index > 0:
            col_index = col + 1
            while col_index > 0:
                region_sum += self.bit_2d[row_index][col_index]
                col_index -= col_index & (-col_index)
            row_index -= row_index & (-row_index)
        return region_sum

    # -----> Time Complexity: O(log(m) * log(n))
    def update(self, row, col, val):
        self.update_tree_val(row, col, val - self.matrix[row][col])
        self.matrix[row][col] = val

    # -----> Time Complexity: O(log(m) * log(n))
    def sumRegion(self, row1, col1, row2, col2):
        return self.get_sum(row2, col2) - self.get_sum(row1 - 1, col2) - self.get_sum(row2, col1 - 1) + self.get_sum(row1 - 1, col1 - 1)

print(f"origin matrix: {[[1, 2, 3], [3, 4, 5]]}")
num_matrix = NumMatrix([[1, 2, 3], [3, 4, 5]])
print(f"num_matrix.sumRegion(0, 0, 1, 1) == 10, correct: {num_matrix.sumRegion(0, 0, 1, 1) == 10}")
print(f"num_matrix.sumRegion(0, 1, 1, 2) == 14, correct: {num_matrix.sumRegion(0, 1, 1, 2) == 14}")
print("num_matrix.update(1, 2, 2)")
num_matrix.update(1, 2, 2)
print(f"num_matrix.sumRegion(0, 1, 1, 2) == 11, correct: {num_matrix.sumRegion(0, 1, 1, 2) == 11}")
print("num_matrix.update(1, 1, 9)")
num_matrix.update(1, 1, 9)
print(f"num_matrix.sumRegion(0, 1, 1, 2) == 16, correct: {num_matrix.sumRegion(0, 1, 1, 2) == 16}")
