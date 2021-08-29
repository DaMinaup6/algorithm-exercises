// -----------------------------------------
// Model Solution: Dynamic Programming
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := binary.size()
//
// Ref: https://leetcode.com/problems/number-of-unique-good-subsequences/discuss/1431819/JavaC%2B%2BPython-DP-4-lines-O(N)-Time-O(1)-Space

class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        int ugs_ends_with_0 = 0;
        int ugs_ends_with_1 = 0;

        bool has_zero = false;
        for (const char bit : binary) {
            if (bit == '0') {
                has_zero = true;
                ugs_ends_with_0 = (ugs_ends_with_0 + ugs_ends_with_1) % MOD;
            } else {
                ugs_ends_with_1 = (ugs_ends_with_0 + ugs_ends_with_1 + 1) % MOD;
            }
        }

        return (ugs_ends_with_0 + ugs_ends_with_1 + (has_zero ? 1 : 0)) % MOD;
    }

private:
    static const int MOD = 1e9 + 7;
};
