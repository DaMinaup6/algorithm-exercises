// -----------------------------------------
// My Solution
//
// Time  Complexity: O(mn)
// Space Complexity: O(1)
// -----------------------------------------
// m := mat.size(), n := mat[0].size()
//
// Note: No extra space is required other than the space used to store the output
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int row_size = mat.size(), col_size = mat[0].size();
        vector<vector<int>> distance_matrix(row_size, vector<int>(col_size));

        for (int row = 0; row < row_size; ++row) {
            for (int col = 0; col < col_size; ++col) {
                if (mat[row][col] == 1) {
                    if (row - 1 >= 0 && mat[row - 1][col] == 0)
                        distance_matrix[row][col] = 1;
                    if (col - 1 >= 0 && mat[row][col - 1] == 0)
                        distance_matrix[row][col] = 1;
                    if (row + 1 < row_size && mat[row + 1][col] == 0)
                        distance_matrix[row][col] = 1;
                    if (col + 1 < col_size && mat[row][col + 1] == 0)
                        distance_matrix[row][col] = 1;
                }
            }
        }

        for (int row = 0; row < row_size; ++row) {
            for (int col = 0; col < col_size; ++col) {
                if (mat[row][col] == 1 && distance_matrix[row][col] != 1) {
                    vector<int> distances = {INT_MAX - 1};
                    if (row - 1 >= 0 && distance_matrix[row - 1][col] > 0)
                        distances.push_back(distance_matrix[row - 1][col]);
                    if (col - 1 >= 0 && distance_matrix[row][col - 1] > 0)
                        distances.push_back(distance_matrix[row][col - 1]);
                    if (row + 1 < row_size && distance_matrix[row + 1][col] > 0)
                        distances.push_back(distance_matrix[row + 1][col]);
                    if (col + 1 < col_size && distance_matrix[row][col + 1] > 0)
                        distances.push_back(distance_matrix[row][col + 1]);
                    distance_matrix[row][col] = *min_element(distances.begin(), distances.end()) + 1;
                }
            }
        }

        for (int row = row_size - 1; row >= 0; --row) {
            for (int col = col_size - 1; col >= 0; --col) {
                if (mat[row][col] == 1 && distance_matrix[row][col] != 1) {
                    vector<int> distances = {INT_MAX - 1};
                    if (row - 1 >= 0 && distance_matrix[row - 1][col] > 0)
                        distances.push_back(distance_matrix[row - 1][col]);
                    if (col - 1 >= 0 && distance_matrix[row][col - 1] > 0)
                        distances.push_back(distance_matrix[row][col - 1]);
                    if (row + 1 < row_size && distance_matrix[row + 1][col] > 0)
                        distances.push_back(distance_matrix[row + 1][col]);
                    if (col + 1 < col_size && distance_matrix[row][col + 1] > 0)
                        distances.push_back(distance_matrix[row][col + 1]);
                    distance_matrix[row][col] = *min_element(distances.begin(), distances.end()) + 1;
                }
            }
        }

        return distance_matrix;
    }
};

// -----------------------------------------
// Model Solution: Dynamic Programming
//
// Time  Complexity: O(mn)
// Space Complexity: O(1)
// -----------------------------------------
// m := mat.size(), n := mat[0].size()
//
// Ref:  https://leetcode.com/problems/01-matrix/solution/
// Note: No extra space is required other than the space used to store the output
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int row_size = mat.size();
        int col_size = mat[0].size();
        vector<vector<int>> distance_matrix(row_size, vector<int> (col_size, INT_MAX - 100000));

        // First pass: check for left and top
        for (int row = 0; row < row_size; ++row) {
            for (int col = 0; col < col_size; ++col) {
                if (mat[row][col] == 0) {
                    distance_matrix[row][col] = 0;
                } else {
                    if (row > 0)
                        distance_matrix[row][col] = min(distance_matrix[row][col], distance_matrix[row - 1][col] + 1);
                    if (col > 0)
                        distance_matrix[row][col] = min(distance_matrix[row][col], distance_matrix[row][col - 1] + 1);
                }
            }
        }

        // Second pass: check for bottom and right
        for (int row = row_size - 1; row >= 0; --row) {
            for (int col = col_size - 1; col >= 0; --col) {
                if (row < row_size - 1)
                    distance_matrix[row][col] = min(distance_matrix[row][col], distance_matrix[row + 1][col] + 1);
                if (col < col_size - 1)
                    distance_matrix[row][col] = min(distance_matrix[row][col], distance_matrix[row][col + 1] + 1);
            }
        }
        return distance_matrix;
    }
};
