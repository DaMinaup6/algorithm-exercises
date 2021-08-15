// -----------------------------------------
// My Solution: Sliding Window
//
// Time  Complexity: O(m + n)
// Space Complexity: O(m + n)
// -----------------------------------------
// m := s.size(), n := t.size()
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, size_t> char_needed_count;
        size_t unique_char_count = 0;
        for (auto letter : t) {
            if (char_needed_count.find(letter) == char_needed_count.end())
                ++unique_char_count;
            ++char_needed_count[letter];
        }

        unordered_map<char, size_t> curr_char_count;
        size_t filled_char_count = 0;
        size_t curr_right_cursor = 0;
        size_t output_str_left   = 0;
        size_t output_str_right  = s.size() + 1;
        for (size_t index = 0; index < s.size(); ++index) {
            while (filled_char_count < unique_char_count && curr_right_cursor < s.size()) {
                ++curr_char_count[s[curr_right_cursor]];
                if (curr_char_count[s[curr_right_cursor]] == char_needed_count[s[curr_right_cursor]])
                    ++filled_char_count;
                ++curr_right_cursor;
            }

            if (filled_char_count == unique_char_count && (curr_right_cursor - index < output_str_right - output_str_left)) {
                output_str_left  = index;
                output_str_right = curr_right_cursor;
            }

            if (curr_char_count[s[index]] == char_needed_count[s[index]])
                --filled_char_count;
            --curr_char_count[s[index]];
        }

        if (output_str_right == s.size() + 1)
            return "";
        return s.substr(output_str_left, output_str_right - output_str_left);
    }
};
