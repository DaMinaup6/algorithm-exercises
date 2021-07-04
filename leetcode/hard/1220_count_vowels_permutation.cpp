// -----------------------------------------
// My Solution: Dynamic Programming
//
// Time  complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
class Solution {
public:
    int countVowelPermutation(int n) {
        // 'a' can be placed after 'e', 'i' and 'u', 'e' can be placed after 'a' and 'i', and so on
        unordered_map<char, string> char_follow_chars_mapping = {{'a', "eiu"}, {'e', "ai"}, {'i', "eo"}, {'o', "i"}, {'u', "io"}};
        unordered_map<char, int> curr_vowels_count = {{'a', 1}, {'e', 1}, {'i', 1}, {'o', 1}, {'u', 1}};

        for (int index = 1; index < n; ++index) {
            unordered_map<char, int> next_vowels_count = {{'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}};
            for (auto &key_value : char_follow_chars_mapping) {
                char curr_char = key_value.first;

                string follow_chars = key_value.second;
                for (auto &follow_char : follow_chars)
                    next_vowels_count[curr_char] = (next_vowels_count[curr_char] + curr_vowels_count[follow_char]) % MOD;
            }
            curr_vowels_count = next_vowels_count;
        }

        int total_permutations = 0;
        total_permutations = (total_permutations + curr_vowels_count['a']) % MOD;
        total_permutations = (total_permutations + curr_vowels_count['e']) % MOD;
        total_permutations = (total_permutations + curr_vowels_count['i']) % MOD;
        total_permutations = (total_permutations + curr_vowels_count['o']) % MOD;
        total_permutations = (total_permutations + curr_vowels_count['u']) % MOD;
        return total_permutations;
    }

private:
    static const int MOD = 1e9 + 7;
};

// -----------------------------------------
// Model Solution: Matrix Multiplication
//
// Time  complexity: O(log(n))
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1220-count-vowels-permutation/
class Solution {
public:
    int countVowelPermutation(int n) {
        vector<vector<long>> state_matrix({
            {0, 1, 0, 0, 0}, // a
            {1, 0, 1, 0, 0}, // e
            {1, 1, 0, 1, 1}, // i
            {0, 0, 1, 0, 1}, // o
            {1, 0, 0, 0, 0}, // u
        });
        vector<vector<long>> permutations_count{{1}, {1}, {1}, {1}, {1}};

        n -= 1;
        while (n > 0) {
            if (n % 2 == 1)
                permutations_count = matrix_multiply(state_matrix, permutations_count);
            state_matrix = matrix_multiply(state_matrix, state_matrix);
            n /= 2;
        }

        long total_permutations = 0;
        for (int index = 0; index < 5; ++index)
            total_permutations += permutations_count[index][0];
        return total_permutations % MOD;
    }

private:
    static const int MOD = 1e9 + 7;

    vector<vector<long>> matrix_multiply(const vector<vector<long>>& matrix_1, const vector<vector<long>>& matrix_2) {
        int matrix_1_row_size = matrix_1.size();
        int matrix_1_col_size = matrix_1[0].size();
        int matrix_2_col_size = matrix_2[0].size();

        vector<vector<long>> result_matrix(matrix_1_row_size, vector<long>(matrix_2_col_size));
        for (int matrix_1_row = 0; matrix_1_row < matrix_1_row_size; ++matrix_1_row) {
            for (int matrix_2_col = 0; matrix_2_col < matrix_2_col_size; ++matrix_2_col) {
                for (int matrix_1_col = 0; matrix_1_col < matrix_1_col_size; ++matrix_1_col)
                    result_matrix[matrix_1_row][matrix_2_col] += matrix_1[matrix_1_row][matrix_1_col] * matrix_2[matrix_1_col][matrix_2_col];
                result_matrix[matrix_1_row][matrix_2_col] %= MOD;
            }
        }
        return result_matrix;
    }
};
