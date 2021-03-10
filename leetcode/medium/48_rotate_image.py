# -----------------------------------------
# My Solution
# -----------------------------------------
# class Solution:
#     def rotate(self, matrix):
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         l = 0
#         while n > 1:
#             # rotate outside matrix
#             for idx in range(0, n - 1):
#                 matrix[                l][          idx + l], \
#                 matrix[          idx + l][(n - 1)       + l], \
#                 matrix[(n - 1) - idx + l][                l], \
#                 matrix[(n - 1)       + l][(n - 1) - idx + l]  \
#                 = \
#                 matrix[(n - 1) - idx + l][                l], \
#                 matrix[                l][          idx + l], \
#                 matrix[(n - 1)       + l][(n - 1) - idx + l], \
#                 matrix[          idx + l][(n - 1)       + l]
#
#             n -= 2 # reduce matrix to inner matrix, for example there is a 3 x 3 matrix inside 5 x 5 matrix so need minus 2
#             l += 1 # for 3 x 3 matrix inside 5 x 5 matrix, its position need to add 1, e.g. [0, 0] -> [1, 1]

# -----------------------------------------
# Model Solution
# -----------------------------------------
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1 - Transpose Matrix: swap(matrix[i][j], matrix[j][i])
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2 - Flip Horizontally: swap(matrix[i][j], matrix[i][n - 1 - j])
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]
