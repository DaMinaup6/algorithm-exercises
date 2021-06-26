// -----------------------------------------
// Model Solution: XOR
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := t.size() == s.size() + 1
// Ref: https://leetcode.com/problems/find-the-difference/discuss/594653/C%2B%2B-XOR
class Solution {
public:
    char findTheDifference(string s, string t) {
        int xor_val = 0;

        // value of xor of two same numbers is 0, i.e. 2 ^ 2 == 0
        // so the xor value of all characters would be the extra character
        for (int index = 0; index < s.size(); ++index) {
            xor_val ^= (s[index] - 'a') ^ (t[index] - 'a');
        }
        xor_val ^= (t[t.size() - 1] - 'a');
        return xor_val + 'a';
    }
};
