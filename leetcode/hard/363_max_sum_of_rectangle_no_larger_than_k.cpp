// -----------------------------------------
// My Solution
//
// Time  Complexity: O((mn)^2)
// Space Complexity: O(mn)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size()
// Note: This solution passes all test cases but took too long
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int row_size = matrix.size(), col_size = matrix[0].size();

        integral = vector<vector<int>>(row_size + 1, vector<int>(col_size + 1));
        for (int row = 0; row < row_size; ++row) {
            for (int col = 0; col < col_size; ++col) {
                integral[row + 1][col + 1] = matrix[row][col] + integral[row + 1][col] + integral[row][col + 1] - integral[row][col];
            }
        }
        
        int max_sum = INT_MIN;
        for (int row = 0; row < row_size; ++row) {
            for (int col = 0; col < col_size; ++col) {
                for (int sub_row = row; sub_row < row_size; ++sub_row) {
                    for (int sub_col = col; sub_col < col_size; ++sub_col) {
                        int curr_sum = range_sum(row, col, sub_row, sub_col);
                        if (curr_sum == k)
                            return k;
                        if (curr_sum < k)
                            max_sum = max(max_sum, curr_sum);
                    }
                }
            }
        }
        return max_sum;
    }

    int range_sum(int row_1, int col_1, int row_2, int col_2) {
        return integral[row_2 + 1][col_2 + 1] - integral[row_2 + 1][col_1] - integral[row_1][col_2 + 1] + integral[row_1][col_1];
    }

private:
    vector<vector<int>> integral;
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(m^2 * nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size()
// Ref: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
class Solution {
public:
    int result = INT_MIN;

    void update_result(vector<int>& nums, int k) {
        int sum = 0;

        // Container to store sorted prefix sums.
        set<int> sorted_set;

        // Add 0 as the prefix sum for an empty sub-array.
        sorted_set.insert(0);
        for (int& num : nums) {
            // Running Sum.
            sum += num;

            // Get X where Running sum - X <= k such that sum - X is closest to k.
            set<int>::iterator it = sorted_set.lower_bound(sum - k);

            // If such X is found in the prefix sums.
            // Get the sum of that sub array and update the global maximum resul.
            if (it != sorted_set.end())
                result = max(result, sum - *it);

            // Insert the current running sum to the prefix sums container.
            sorted_set.insert(sum);
        }
    }

    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        // Stores the 1D representation of the matrix.
        vector<int> row_sum(matrix[0].size());

        for (int row_1 = 0; row_1 < matrix.size(); ++row_1) {
            // Initialize the 1D representation with 0s.
            fill(row_sum.begin(), row_sum.end(), 0);

            // We convert the matrix between rows row_1..row_2 inclusive to 1D array
            for (int row_2 = row_1; row_2 < matrix.size(); ++row_2) {
                // Add the current row_2 to the previous row_2.
                // This converts the matrix between row_1..row_2 to 1D array
                for (int col = 0; col < matrix[0].size(); ++col)
                    row_sum[col] += matrix[row_2][col];

                // Run the 1D algorithm for `row_sum`
                update_result(row_sum, k);

                // If result is k, this is the best possible answer, so return.
                if (result == k)
                    return result;
            }
        }
        return result;
    }
};

// -----------------------------------------
// Model Solution: Use Kadane's algorithm to reduce time for some cases
//
// Time  Complexity: O(i^2 * alog(a))
// Space Complexity: O(a)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size(), i := min(m, n), a := max(m, n)
// Ref: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
class Solution {
public:
    int result = INT_MIN;

    // Standard Kadane's algorithm.
    int get_max_kadane(vector<int>& nums) {
        int max_kadane = INT_MIN, current_max_sum = 0;
        for (int& num : nums) {
            current_max_sum = max(current_max_sum + num, num);
            max_kadane = max(max_kadane, current_max_sum);
        }
        return max_kadane;
    }

    void update_result(vector<int>& nums, int k) {
        int kadane_sum = get_max_kadane(nums);

        // If max possible sum of any subarray of nums is <= k
        // use that result to compare with gobal maxium result and return
        if (kadane_sum <= k) {
            result = max(result, kadane_sum);
            return;
        }
        int sum = 0;

        // Container to store sorted prefix sums.
        set<int> sorted_sum;

        // Add 0 as the prefix sum for an empty sub-array.
        sorted_sum.insert(0);
        for (int& num : nums) {
            // Running Sum.
            sum += num;

            // Get X where Running sum - X <= k such that sum - X is closest to k.
            set<int>::iterator it = sorted_sum.lower_bound(sum - k);

            // If such X is found in the prefix sums.
            // Get the sum of that sub array and update the global maximum result.
            if (it != sorted_sum.end())
                result = max(result, sum - *it);

            // Insert the current running sum to the prefix sums container.
            sorted_sum.insert(sum);
        }
    }

    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if (matrix[0].size() > matrix.size()) {
            // Stores the 1D representation of the matrix row wise.
            vector<int> rowSum(matrix[0].size());
            for (int i = 0; i < matrix.size(); i++) {
                // Initialize the 1D representation with 0s.
                fill(rowSum.begin(), rowSum.end(), 0);

                // We convert the matrix between rows i..row inclusive to 1D array
                for (int row = i; row < matrix.size(); row++) {
                    // Add the current row to the previous row.
                    // This converts the matrix between i..j to 1D array
                    for (int col = 0; col < matrix[0].size(); col++)
                        rowSum[col] += matrix[row][col];

                    // Run the 1D algorithm for `rowSum`
                    update_result(rowSum, k);

                    // If result is k, this is the best possible answer, so return.
                    if (result == k)
                        return result;
                }
            }
        } else {
            // Stores the 1D representation of the matrix column wise.
            vector<int> colSum(matrix.size());
            for (int i = 0; i < matrix[0].size(); i++) {
                // Initialize the 1D representation with 0s.
                fill(colSum.begin(), colSum.end(), 0);

                // We convert the matrix between columns i..col inclusive to 1D array
                for (int col = i; col < matrix[0].size(); col++) {
                    // Add the current column to the previous column.
                    for (int row = 0; row < matrix.size(); row++)
                        colSum[row] += matrix[row][col];

                    // Run the 1D algorithm for `colSum`
                    update_result(colSum, k);

                    // If Max is k, this is the best possible answer, so return.
                    if (result == k)
                        return result;
                }
            }
        }
        return result;
    }
};
