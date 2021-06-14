// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()
#include <string>

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> char_num_mapping = {{ 'I', 1 }, { 'V', 5 }, { 'X', 10 }, { 'L', 50 }, { 'C', 100 }, { 'D', 500 }, { 'M', 1000 }};

        int represent_integer = 0;
        int string_cursor_pos = 0;
        while (string_cursor_pos < s.size()) {
            if (string_cursor_pos < s.size() - 1 && char_num_mapping[s[string_cursor_pos]] < char_num_mapping[s[string_cursor_pos + 1]]) {
                represent_integer += char_num_mapping[s[string_cursor_pos + 1]] - char_num_mapping[s[string_cursor_pos]];
                string_cursor_pos += 2;
            } else {
                represent_integer += char_num_mapping[s[string_cursor_pos]];
                string_cursor_pos += 1;
            }
        }
        return represent_integer;
    }
};
