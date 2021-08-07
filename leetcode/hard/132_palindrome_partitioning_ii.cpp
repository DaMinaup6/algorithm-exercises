// -----------------------------------------
// Model Solution: Dynamic Programming
//
// Time  Complexity: O(n^2)
// Space Complexity: O(n)
// -----------------------------------------
// n := s.size()
//
// Ref:
// a) https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-132-palindrome-partitioning-ii/
// b) https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42205/56-ms-python-with-explanation

class Solution {
public:
    int minCut(string s) {
        int str_size = s.size();

        vector<int> min_cuts;
        for (int cuts = -1; cuts < str_size; ++cuts)
            min_cuts.push_back(cuts);

        for (int index = 0; index < str_size; ++index) {
            int left_cursor  = index;
            int right_cursor = index;
            while (left_cursor >= 0 && right_cursor < str_size && s[left_cursor] == s[right_cursor]) {
                min_cuts[right_cursor + 1] = min(min_cuts[right_cursor + 1], min_cuts[left_cursor] + 1);
                --left_cursor;
                ++right_cursor;
            }

            left_cursor  = index;
            right_cursor = index + 1;
            while (left_cursor >= 0 && right_cursor < str_size && s[left_cursor] == s[right_cursor]) {
                min_cuts[right_cursor + 1] = min(min_cuts[right_cursor + 1], min_cuts[left_cursor] + 1);
                --left_cursor;
                ++right_cursor;
            }
        }

        return min_cuts.back();
    }
};
