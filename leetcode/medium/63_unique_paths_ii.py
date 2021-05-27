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

        # According to the solution, number of ways to reach some position (i, j), defined as dp[i][j],
        # equals dp[i - 1][j] + dp[i][j - 1] (since we can either go right or down)
        # but this can be simplified by using one-dimensional array
        #
        # e.g. obstacleGrid == [[0,0,1,0],[0,0,0,0],[1,1,1,0],[0,0,0,0]]
        # after gone through first row, dp would be [1, 1, 0, 0]
        # for position dp[1][1], it equals dp[0][1] + dp[1][0]
        # but now we just use dp again in second row, so dp[0][1] already contained in dp[1], then we need to only
        # add dp[0]
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1] if j > 0 else 0
            print('dp:', dp)
        return dp[-1]
