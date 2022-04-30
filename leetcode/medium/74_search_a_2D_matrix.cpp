// -----------------------------------------
// My Solution
//
// Time  Complexity: O(log(mn))
// Space Complexity: O(1)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size()

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row_cursor_1 = 0;
        int row_cursor_2 = matrix.size() - 1;
        while (row_cursor_1 <= row_cursor_2) {
            int middle_cursor = (row_cursor_1 + row_cursor_2) / 2;
            if (target >= matrix[middle_cursor][0]) {
                row_cursor_1 = middle_cursor + 1;
            } else {
                row_cursor_2 = middle_cursor - 1;
            }
        }

        if (row_cursor_2 < 0) {
            return false;
        } else if (matrix[row_cursor_2][0] == target) {
            return true;
        }

        int col_cursor_1 = 0;
        int col_cursor_2 = matrix[row_cursor_2].size() - 1;
        while (col_cursor_1 <= col_cursor_2) {
            int middle_cursor = (col_cursor_1 + col_cursor_2) / 2;
            if (target >= matrix[row_cursor_2][middle_cursor]) {
                col_cursor_1 = middle_cursor + 1;
            } else {
                col_cursor_2 = middle_cursor - 1;
            }
        }

        if (col_cursor_2 < 0) {
            return false;
        }
        return matrix[row_cursor_2][col_cursor_2] == target;
    }
};
