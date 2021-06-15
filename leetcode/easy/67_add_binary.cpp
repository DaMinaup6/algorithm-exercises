// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := max(a.size(), b.size())
#include <string>

class Solution {
public:
    string addBinary(string a, string b) {
        string binary_string = "";
        int a_index = a.size() - 1, b_index = b.size() - 1, carry = 0;
        while (a_index >= 0 || b_index >= 0 || carry > 0) {
            carry += (a_index >= 0) ? (a[a_index] - '0') : 0;
            carry += (b_index >= 0) ? (b[b_index] - '0') : 0;
            binary_string = char(carry % 2 + '0') + binary_string;
            carry /= 2;

            --a_index;
            --b_index;
        }

        return binary_string;
    }
};
