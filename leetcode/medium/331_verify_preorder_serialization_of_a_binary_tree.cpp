// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := preorder.size()
//
// Ref: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/1426956/Python3Java-Easy-Solution-Explained-in-Detail-or-O(1)-Space

class Solution {
public:
    bool isValidSerialization(string preorder) {
        stringstream str_stream(preorder);
        string curr_str;

        int slots = 1;
        while (getline(str_stream, curr_str, ',')) {
            if (slots <= 0)
                return false;

            if (curr_str == "#")
                --slots;
            else
                ++slots;
        }

        return slots == 0;
    }
};
