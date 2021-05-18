# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(matrix)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        curr_dp = matrix[0]
        for row in range(1, n):
            next_dp = [0] * n
            for col in range(n):
                possible_paths = [curr_dp[col]]
                if col > 0:
                    possible_paths.append(curr_dp[col - 1])
                if col < n - 1:
                    possible_paths.append(curr_dp[col + 1])
                next_dp[col] = matrix[row][col] + min(possible_paths)
            curr_dp = next_dp
        return min(curr_dp)
