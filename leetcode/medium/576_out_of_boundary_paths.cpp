// -----------------------------------------
// My Solution
//
// Time  Complexity: O(mnr^2)
// Space Complexity: O(mnr)
// -----------------------------------------
// r := maxMove
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        row_size = m;
        col_size = n;
        count_paths_cache = vector<vector<vector<int>>>(m + 1, vector<vector<int>>(n + 1, vector<int>(maxMove + 1, -1)));

        long long total_paths = 0;
        for (int remain_moves = 1; remain_moves <= maxMove; ++remain_moves)
            total_paths = (total_paths + count_paths(startRow, startColumn, remain_moves)) % MOD;
        return total_paths;
    }

private:
    const int MOD = 1e9 + 7;
    const int position_moves[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

    int row_size;
    int col_size;
    vector<vector<vector<int>>> count_paths_cache;

    bool position_valid(int row, int col) {
        return 0 <= row && row < row_size && 0 <= col && col < col_size;
    }

    long long count_paths(int row, int col, int remain_moves) {
        if (remain_moves == 0)
            return 0;
        if (count_paths_cache[row][col][remain_moves] != -1)
            return count_paths_cache[row][col][remain_moves];

        long long paths = 0;
        for (auto& move : position_moves) {
            int next_row = row + move[0];
            int next_col = col + move[1];
            if (remain_moves == 1 && !position_valid(next_row, next_col)) {
                ++paths;
            } else if (remain_moves > 1 && position_valid(next_row, next_col)) {
                paths = (paths + count_paths(next_row, next_col, remain_moves - 1)) % MOD;
            }
        }

        count_paths_cache[row][col][remain_moves] = paths;
        return paths;
    }
};

// -----------------------------------------
// My Solution: Dynamic Programming
//
// Time  Complexity: O(mnr)
// Space Complexity: O(mn)
// -----------------------------------------
// r := maxMove
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1e9 + 7;
        const int position_moves[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

        vector<vector<int>> curr_dp(m, vector<int>(n, 0));
        for (int moves = 1; moves <= maxMove; ++moves) {
            vector<vector<int>> next_dp(m, vector<int>(n, 0));
            for (int row = 0; row < m; ++row) {
                for (int col = 0; col < n; ++col) {
                    if (row == 0)
                        ++next_dp[row][col];
                    if (col == 0)
                        ++next_dp[row][col];
                    if (row == m - 1)
                        ++next_dp[row][col];
                    if (col == n - 1)
                        ++next_dp[row][col];

                    for (auto& move : position_moves) {
                        int prev_row = row + move[0];
                        int prev_col = col + move[1];
                        if (0 <= prev_row && prev_row < m && 0 <= prev_col && prev_col < n)
                            next_dp[row][col] = (next_dp[row][col] + curr_dp[prev_row][prev_col]) % MOD;
                    }
                }
            }

            curr_dp = next_dp;
        }
        return curr_dp[startRow][startColumn];
    }
};
