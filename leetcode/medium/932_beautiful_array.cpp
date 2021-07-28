// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// Ref: https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
class Solution {
public:
    vector<int> beautifulArray(int n) {
        vector<int> beautiful_array = {1};
        while (beautiful_array.size() < n) {
            vector<int> tmp_array;

            for (int& num: beautiful_array) {
                if (num * 2 <= n)
                    tmp_array.push_back(num * 2);
            }

            for (int& num: beautiful_array) {
                if (num * 2 - 1 <= n)
                    tmp_array.push_back(num * 2 - 1);
            }

            beautiful_array = tmp_array;
        }

        return beautiful_array;
    }
};
