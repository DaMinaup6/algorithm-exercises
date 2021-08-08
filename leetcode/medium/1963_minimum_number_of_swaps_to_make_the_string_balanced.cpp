// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()

class Solution {
public:
    int minSwaps(string s) {
        int right_cursor = s.size() - 1;
        int open_brackets_count = 0;
        int swaps = 0;
        for (int index = 0; index < right_cursor; ++index) {
            open_brackets_count += (s[index] == '[') ? 1 : -1;
            if (open_brackets_count < 0) {
                while (s[right_cursor] == ']')
                    --right_cursor;

                swap(s[index], s[right_cursor]);
                ++swaps;
                open_brackets_count = 1;
            }
        }

        return swaps;
    }
};
