// -----------------------------------------
// Model Solution: Dynamic Programming
//
// Time  Complexity: O(n^2)
// Space Complexity: O(n^2)
// -----------------------------------------
// Ref: https://leetcode.com/problems/largest-plus-sign/discuss/1453639/C%2B%2B-Simple-Dynamic-Programming-Solution-With-Explanation
class Solution {
public:
    void fillDP(vector<vector<int>>& dp, vector<vector<int>>& mat, int n) {
        int down, right, up, left;

        for (int i = 0; i < n; i++) {
            down = 0, right = 0;

            for (int j = 0; j < n; j++) {
                right = mat[i][j] ? right+1 : 0;
                dp[i][j] = min(dp[i][j], right);

                down = mat[j][i] ? down+1 : 0;
                dp[j][i] = min(dp[j][i], down);
            }
        }

        for (int i = 0; i < n; i++) {
            up = 0, left = 0;
            for (int j = n-1; j >= 0; j--) {
                left = mat[i][j] ? left+1 : 0;
                dp[i][j] = min(dp[i][j], left);

                up = mat[j][i] ? up+1 : 0;
                dp[j][i] = min(dp[j][i], up);
            }
        }
    }

    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        vector<vector<int>> mat(n, vector<int>(n, 1));

        for (auto mine : mines)
            mat[mine[0]][mine[1]] = 0;

        fillDP(dp, mat, n);

        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res = max(res, dp[i][j]);
            }
        }
        return res;
    }
};
