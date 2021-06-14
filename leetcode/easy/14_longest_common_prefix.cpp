// -----------------------------------------
// My Solution
//
// Time  Complexity: O(mn)
// Space Complexity: O(m)
// -----------------------------------------
// m := max string size in strs, n := strs.size()
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string longest_common_prefix = "";
        int str_cursor_position = 0;
        while (true) {
            char curr_char = '\0';
            for (int index = 0; index < strs.size(); ++index) {
                if (str_cursor_position >= strs[index].size())
                    return longest_common_prefix;

                if (curr_char == '\0') {
                    curr_char = strs[index][str_cursor_position];
                } else if (strs[index][str_cursor_position] != curr_char) {
                    return longest_common_prefix;
                }
            }

            longest_common_prefix += curr_char;
            str_cursor_position += 1;
        }
    }
};
