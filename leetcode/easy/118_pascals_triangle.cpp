// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n^2)
// Space Complexity: O(n^2)
// -----------------------------------------
// n := numRows
// Ref: https://leetcode.com/problems/pascals-triangle/discuss/38171/Maybe-shortest-c%2B%2B-solution
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascal_triangle(numRows);
        for (int layer = 0; layer < numRows; ++layer) {
            pascal_triangle[layer].resize(layer + 1);
            pascal_triangle[layer][0] = pascal_triangle[layer][layer] = 1;
            for (int cell_index = 1; cell_index < layer; ++cell_index) {
                pascal_triangle[layer][cell_index] = pascal_triangle[layer - 1][cell_index - 1] + pascal_triangle[layer - 1][cell_index];
            }
        }
        
        return pascal_triangle;
    }
};
