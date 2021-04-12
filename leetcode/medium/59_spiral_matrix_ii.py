# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]

        curr_direction = 'R'
        curr_num = 1
        last_num = pow(n, 2)
        i = j = 0
        while curr_num <= last_num:
            matrix[i][j] = curr_num
            if curr_direction == 'R':
                if j < n - 1 and matrix[i][j + 1] == -1:
                    j += 1
                else:
                    curr_direction = 'D'
                    i += 1
            elif curr_direction == 'D':
                if i < n - 1 and matrix[i + 1][j] == -1:
                    i += 1
                else:
                    curr_direction = 'L'
                    j -= 1
            elif curr_direction == 'L':
                if j > 0 and matrix[i][j - 1] == -1:
                    j -= 1
                else:
                    curr_direction = 'U'
                    i -= 1
            elif curr_direction == 'U':
                if i > 0 and matrix[i - 1][j] == -1:
                    i -= 1
                else:
                    curr_direction = 'R'
                    j += 1

            curr_num += 1

        return matrix
