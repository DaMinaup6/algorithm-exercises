// -----------------------------------------
// Model Solution: Mathematical
//
// Time  Complexity: O(n^2)
// Space Complexity: O(n)
// -----------------------------------------
// n := s.size()
//
// Ref: https://leetcode.com/problems/orderly-queue/solution/
class Solution {
public:
    string orderlyQueue(string s, int k) {
        if (k == 1) {
            string min_str = s;
            for (int index = 1; index < s.size(); ++index)
                min_str = min(min_str, s.substr(index) + s.substr(0, index));
            return min_str;
        }

        sort(s.begin(), s.end());
        return s;
    }
};
