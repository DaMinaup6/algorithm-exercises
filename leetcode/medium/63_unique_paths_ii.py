# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(obstacleGrid), n := len(obstacleGrid[0])
# Ref: https://leetcode.com/problems/unique-paths-ii/solution/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == j == 0:
                    dp[i][j] = 1
                
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and obstacleGrid[i - 1][j] == 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0 and obstacleGrid[i][j - 1] == 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(n)
# -----------------------------------------
# m := len(obstacleGrid), n := len(obstacleGrid[0])
# Ref: https://leetcode.com/problems/unique-paths-ii/solution/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp_curr = [0] * len(obstacleGrid[0])
        dp_curr[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp_curr[j] = 0
                else:
                    dp_curr[j] += dp_curr[j - 1] if j > 0 else 0

        return dp_curr[-1]
