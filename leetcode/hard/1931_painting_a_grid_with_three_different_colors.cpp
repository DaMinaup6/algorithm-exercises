// -----------------------------------------
// Model Solution
//
// Time  Complexity: O((k^2) * mn + k)
// Space Complexity: O(k)
// -----------------------------------------
// k := 3 * 2^(m - 1)
//
// Ref:  https://www.youtube.com/watch?v=YNOy0CCIDjE
// Note: This is a relatively slow solution but easier to understand and it passes all test cases at least
class Solution {
public:
    int colorTheGrid(int m, int n) {
        row_num = m;
        col_num = n;

        vector<int> curr_state;
        generate_states(curr_state);

        vector<int> curr_dp(state_index_state_map.size(), 1);
        vector<int> next_dp(state_index_state_map.size());
        int valid_grid_states_count = state_index_state_map.size();

        for (int col_index = 1; col_index < col_num; ++col_index) {
            fill(next_dp.begin(), next_dp.end(), 0);
            valid_grid_states_count = 0;

            for (int next_state_index = 0; next_state_index < state_index_state_map.size(); ++next_state_index) {
                for (int curr_state_index = 0; curr_state_index < state_index_state_map.size(); ++curr_state_index) {
                    bool no_adjacent_cells_same_color = true;
                    for (int row_index = 0; row_index < row_num; ++row_index) {
                        if (state_index_state_map[curr_state_index][row_index] == state_index_state_map[next_state_index][row_index]) {
                            no_adjacent_cells_same_color = false;
                            break;
                        }
                    }

                    if (no_adjacent_cells_same_color)
                        next_dp[next_state_index] = (next_dp[next_state_index] + curr_dp[curr_state_index]) % MOD;
                }
                valid_grid_states_count = (valid_grid_states_count + next_dp[next_state_index]) % MOD;
            }
            swap(curr_dp, next_dp);
        }

        return valid_grid_states_count;
    }

    void generate_states(vector<int>& curr_state) {
        if (curr_state.size() == row_num) {
            state_index_state_map[state_index_state_map.size()] = curr_state;
            return;
        }

        for (int num: {0, 1, 2}) {
            if (curr_state.empty() || num != curr_state.back()) {
                curr_state.push_back(num);
                generate_states(curr_state);
                curr_state.pop_back();
            }
        }
    }

private:
    static const int MOD = 1e9 + 7;
    int row_num;
    int col_num;
    unordered_map<int, vector<int>> state_index_state_map;
};

// -----------------------------------------
// Model Solution: Fast Exponentiation
//
// Time  Complexity: O((k^3) * log2(n) + (k^2) * m + k)
// Space Complexity: O(k^2 + k)
// -----------------------------------------
// k := 3 * 2^(m - 1)
//
// Ref:
// a) https://www.youtube.com/watch?v=YNOy0CCIDjE
// b) https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1220-count-vowels-permutation/
class Solution {
public:
    int colorTheGrid(int m, int n) {
        row_num = m;
        col_num = n;

        vector<int> curr_state;
        generate_states(curr_state);
        initialize_state_matrix();

        vector<vector<long>> count_matrix(state_index_state_map.size(), vector<long>(1, 1));
        col_num -= 1;
        while (col_num > 0) {
            if (col_num % 2 == 1)
                count_matrix = matrix_multiply(state_matrix, count_matrix);
            if (col_num > 1)
                state_matrix = matrix_multiply(state_matrix, state_matrix);
            col_num /= 2;
        }

        int valid_grid_states_count = 0;
        for (int index = 0; index < count_matrix.size(); ++index)
            valid_grid_states_count = (valid_grid_states_count + count_matrix[index][0]) % MOD;
        return valid_grid_states_count;
    }

private:
    static const int MOD = 1e9 + 7;
    int row_num;
    int col_num;
    unordered_map<int, vector<int>> state_index_state_map;
    vector<vector<long>> state_matrix;

    void generate_states(vector<int>& curr_state) {
        if (curr_state.size() == row_num) {
            state_index_state_map[state_index_state_map.size()] = curr_state;
            return;
        }

        for (int num: {0, 1, 2}) {
            if (curr_state.empty() || num != curr_state.back()) {
                curr_state.push_back(num);
                generate_states(curr_state);
                curr_state.pop_back();
            }
        }
    }

    void initialize_state_matrix() {
        state_matrix = vector<vector<long>>(state_index_state_map.size(), vector<long>(state_index_state_map.size()));

        for (int next_state_index = 0; next_state_index < state_index_state_map.size(); ++next_state_index) {
            for (int curr_state_index = 0; curr_state_index < state_index_state_map.size(); ++curr_state_index) {
                bool no_adjacent_cells_same_color = true;
                for (int row_index = 0; row_index < row_num; ++row_index) {
                    if (state_index_state_map[curr_state_index][row_index] == state_index_state_map[next_state_index][row_index]) {
                        no_adjacent_cells_same_color = false;
                        break;
                    }
                }

                if (no_adjacent_cells_same_color)
                    state_matrix[next_state_index][curr_state_index] = 1;
            }
        }
    }

    vector<vector<long>> matrix_multiply(const vector<vector<long>>& mat_1, const vector<vector<long>>& mat_2) {
        int mat_1_row_num = mat_1.size();
        int mat_1_col_num = mat_1[0].size();
        int mat_2_col_num = mat_2[0].size();

        vector<vector<long>> res_mat(mat_1_row_num, vector<long>(mat_2_col_num));
        for (int mat_1_row = 0; mat_1_row < mat_1_row_num; ++mat_1_row)
            for (int mat_2_col = 0; mat_2_col < mat_2_col_num; ++mat_2_col)
                for (int mat_1_col = 0; mat_1_col < mat_1_col_num; ++mat_1_col)
                    res_mat[mat_1_row][mat_2_col] = (res_mat[mat_1_row][mat_2_col] + (mat_1[mat_1_row][mat_1_col] * mat_2[mat_1_col][mat_2_col]) % MOD) % MOD;
        return res_mat;
    }
};
