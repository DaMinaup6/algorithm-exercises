#include <bits/stdc++.h>

using namespace std;

static const int MOD = 1e9 + 7;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);
void map_candle_heights_to_rank(vector<vector<int>> &);

class BinaryIndexedTree {
public:
    BinaryIndexedTree(int arr_size): binary_indexed_tree(arr_size + 1, 0) {}

    void update(int index, int delta) {
        while (index < binary_indexed_tree.size()) {
            binary_indexed_tree[index] = (binary_indexed_tree[index] + delta) % MOD;
            index += low_bit(index);
        }
    }

    int query(int index) {
        int range_sum = 0;
        while (index > 0) {
            range_sum = (range_sum + binary_indexed_tree[index]) % MOD;
            index -= low_bit(index);
        }
        return range_sum;
    }

private:
    vector<int> binary_indexed_tree;

    static inline int low_bit(int num) {
        return num & (-num);
    }
};

/*
 * Complete the 'candlesCounting' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. 2D_INTEGER_ARRAY candles
 */

/* -----------------------------------------
 * Model Solution: Bitmask
 *
 * Time  complexity: O(2^k * n^2)
 * Space Complexity: O(2^k * n)
 * -----------------------------------------
 * n := candles.size()
 * Ref:  https://www.hackerrank.com/challenges/candles-2/forum/comments/373962
 * Note: This solution leads to TLE but it's easier to understand
 *
 * int candlesCounting(int k, vector<vector<int>> candles) {
 *     int max_color = 0;
 *     for (int candle_index = 0; candle_index < candles.size(); ++candle_index) {
 *         max_color = max(max_color, candles[candle_index][1]);
 *     }
 *     int color_states = 1 << max_color;
 * 
 *     // dp[i][j] := number of subsequences ending in candle[j] using color state i
 *     vector<vector<int>> dp(color_states, vector<int>(candles.size()));
 *     for (int candle_index = 0; candle_index < candles.size(); ++candle_index)
 *         dp[1 << (candles[candle_index][1] - 1)][candle_index] = 1; // the case where we use only this candle
 * 
 *     for (int candle_index = 0; candle_index < candles.size(); ++candle_index) {
 *         int curr_color_bit = 1 << (candles[candle_index][1] - 1);
 * 
 *         for (int color_state = 1; color_state < color_states; ++color_state) {
 *             if ((color_state & curr_color_bit) == 0) // candle wasn't indeed used
 *                 continue;
 * 
 *             // e.g. k == 2, so our target color state is (11)_2
 *             //      remove color bit of current candle from current color state, say remove (10)_2 from (11)_2, now we get
 *             //      curr_candle_color_removed_state == (01)_2
 *             //      then we check if how many subsequences are there with such color state, then we get total subsequences for (11)_2 color state
 *             //      since those subsequences already have (01)_2 color state, so we get (11)_2 color state after current candle added to those subsequences
 *             //
 *             //      also if target color state was already satisfied in previous candle, also need to add those subsequences to current count
 *             //      of subsequences
 *             int curr_candle_color_removed_state = color_state ^ curr_color_bit;
 *             for (int prev_candle_index = 0; prev_candle_index < candle_index; ++prev_candle_index) {
 *                 if (candles[prev_candle_index][0] < candles[candle_index][0]) {
 *                     dp[color_state][candle_index] += dp[curr_candle_color_removed_state][prev_candle_index] + dp[color_state][prev_candle_index];
 *                     dp[color_state][candle_index] %= MOD;
 *                 }
 *             }
 *         }
 *     }
 * 
 *     int total_subsequences = 0;
 *     for (int candle_index = 0; candle_index < candles.size(); ++candle_index) {
 *         total_subsequences = (total_subsequences + dp[color_states - 1][candle_index]) % MOD;
 *     }
 *     return total_subsequences;
 * }
 *
 * It's easy to see that the bottleneck for this solution is we need to loop through prev_candle_index to sum up the number of subsequences,
 * we can use binary indexed tree to deal with this part to reduce time complexity
 *
 */

/* -----------------------------------------
 * Model Solution: Binary Indexed Tree + Bitmask
 *
 * Time  complexity: O(2^k * nlog(n))
 * Space Complexity: O(2^k * n)
 * -----------------------------------------
 * n := candles.size()
 * Ref: https://iq.opengenus.org/longest-increasing-subsequence-fenwick-tree/
 *
 * int candlesCounting(int k, vector<vector<int>> candles) {
 *     // pre-process
 *     map_candle_heights_to_rank(candles);
 *     int color_states = 1 << k;
 * 
 *     // calculate subsequences count of binary indexed trees in different color state
 *     vector<BinaryIndexedTree> color_state_bit(color_states, BinaryIndexedTree(candles.size()));
 * 
 *     for (int candle_index = 0; candle_index < candles.size(); ++candle_index) {
 *         int height_rank = candles[candle_index][0];
 *         int curr_candle_color_state = 1 << (candles[candle_index][1] - 1);
 * 
 *         for (int color_state = 1; color_state < color_states; ++color_state) {
 *             if ((color_state & curr_candle_color_state) == 0) // candle wasn't indeed used
 *                 continue;
 *             int curr_candle_color_removed_state = color_state ^ curr_candle_color_state;
 * 
 *             int prev_color_state_count = color_state_bit[curr_candle_color_removed_state].query(height_rank - 1);
 *             int curr_color_state_count = color_state_bit[color_state].query(height_rank - 1);
 *             if (color_state == curr_candle_color_state)
 *                 ++curr_color_state_count;
 *             color_state_bit[color_state].update(height_rank, (prev_color_state_count + curr_color_state_count) % MOD);
 *         }
 *     }
 *     return color_state_bit[color_states - 1].query(candles.size());
 * }
 */

/* -----------------------------------------
 * Model Solution: Binary Indexed Tree + Bitmask + Inclusion-Exclusion Principle
 *
 * Time  complexity: O(2^k * nlog(n))
 * Space Complexity: O(n)
 * -----------------------------------------
 * n := candles.size()
 * Ref: https://www.hackerrank.com/challenges/candles-2/editorial
 */
int candlesCounting(int k, vector<vector<int>> candles) {
    map_candle_heights_to_rank(candles);

    int total_subsequences = 0;
    for (int color_state = 1; color_state < (1 << k); ++color_state) {
        BinaryIndexedTree subsequences_counts = BinaryIndexedTree(candles.size());

        int color_state_subsequences_count = 0;
        for (int candle_index = 0; candle_index < candles.size(); ++candle_index) {
            int candle_color_state = 1 << (candles[candle_index][1] - 1);
            if ((color_state & candle_color_state) == 0) // candle wasn't indeed used
                continue;

            int height_rank = candles[candle_index][0];
            int candle_subsequences_count  = (subsequences_counts.query(height_rank - 1) + 1) % MOD;
            color_state_subsequences_count = (color_state_subsequences_count + candle_subsequences_count) % MOD;
            subsequences_counts.update(height_rank, candle_subsequences_count);
        }

        // Inclusion-Exclusion Principle
        if (__builtin_popcount(color_state) % 2 != k % 2)
            color_state_subsequences_count = (MOD - color_state_subsequences_count);
        total_subsequences = (total_subsequences + color_state_subsequences_count) % MOD;
    }
    return total_subsequences;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int k = stoi(first_multiple_input[1]);

    vector<vector<int>> candles(n);

    for (int i = 0; i < n; i++) {
        candles[i].resize(2);

        string candles_row_temp_temp;
        getline(cin, candles_row_temp_temp);

        vector<string> candles_row_temp = split(rtrim(candles_row_temp_temp));

        for (int j = 0; j < 2; j++) {
            int candles_row_item = stoi(candles_row_temp[j]);

            candles[i][j] = candles_row_item;
        }
    }

    int result = candlesCounting(k, candles);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

void map_candle_heights_to_rank(vector<vector<int>>& candles) {
    vector<int> heights;
    for (int candle_index = 0; candle_index < candles.size(); ++candle_index)
        heights.push_back(candles[candle_index][0]);
    sort(heights.begin(), heights.end());

    unordered_map<int, int> height_rank_map;
    for (int index = 0; index < heights.size(); ++index)
        height_rank_map[heights[index]] = index + 1;

    for (int candle_index = 0; candle_index < candles.size(); ++candle_index)
        candles[candle_index][0] = height_rank_map[candles[candle_index][0]];
}
