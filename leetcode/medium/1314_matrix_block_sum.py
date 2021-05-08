# -----------------------------------------
# My Solution
#
# Time  Complexity: O(m^2 * n)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(mat), n := len(mat[0])
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        cumulative_sums = [[0] * n for _ in range(m)]
        for i in range(m):
            cumulative_sums[i][0] = mat[i][0]
        for i in range(m):
            for j in range(1, n):
                cumulative_sums[i][j] = mat[i][j] + cumulative_sums[i][j - 1]

        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for r in range(max(i - k, 0), min(i + k + 1, m)):
                    sum_col = min(j + k, n - 1)
                    if j - k <= 0:
                        answer[i][j] += cumulative_sums[r][sum_col]
                    else:
                        answer[i][j] += cumulative_sums[r][sum_col] - cumulative_sums[r][j - k - 1]
        return answer

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(mat), n := len(mat[0])
# Ref: https://leetcode.com/problems/matrix-block-sum/discuss/1160320/Three-matrix-passes-75-speed
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]
        for r in range(1, m):
            for c in range(n):
                mat[r][c] += mat[r - 1][c]

        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                answer[r][c] = mat[min(r + k, m - 1)][min(c + k, n - 1)]
                if r - k > 0:
                    answer[r][c] -= mat[r - k - 1][min(c + k, n - 1)]
                if c - k > 0:
                    answer[r][c] -= mat[min(r + k, m - 1)][c - k - 1]
                if r - k > 0 and c - k > 0:
                    answer[r][c] += mat[r - k - 1][c - k - 1]
        return answer
