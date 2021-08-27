// -----------------------------------------
// Model Solution
//
// Time  Complexity: O((m^2)nv + mnlog(n))
// Space Complexity: O((m^2)v + mn)
// -----------------------------------------
// m := mat.size(), n := mat[0].size(), v := max(mat[i][j])
//
// Ref: https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1418757/DP-%2B-Pruning-4Sum-II-and-All-Sums

class Solution {
public:
    int dp[71][70 * 70 + 1] = {[0 ... 70][0 ... (70 * 70)] = INT_MAX};

    int dfs(vector<set<int>>& m, int i, int sum, int target) {
        if (i >= m.size())
            return abs(sum - target);

        if (dp[i][sum] == INT_MAX) {
            for (auto it = m[i].begin(); it != m[i].end(); ++it) {
                dp[i][sum] = min(dp[i][sum], dfs(m, i + 1, sum + *it, target));
                if (dp[i][sum] == 0 || sum + *it > target)
                    break;
            }
        }
        return dp[i][sum];
    }

    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
        vector<set<int>> m;
        for (const auto& row : mat)
            m.push_back(set<int>(begin(row), end(row)));
        return dfs(m, 0, 0, target);
    }
};
