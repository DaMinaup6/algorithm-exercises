// -----------------------------------------
// Model Solution: Knuth–Morris–Pratt Pattern Matching (KMP pattern matching)
//
// Time  Complexity: O(m + n)
// Space Complexity: O(m)
// -----------------------------------------
// m := haystack.size(), n := needle.size()
// Ref:
// a) https://www.youtube.com/watch?v=GTJr8OvyEVQ
// b) https://www.youtube.com/watch?v=uKr9qIZMtzw
// c) https://blog.csdn.net/coder_orz/article/details/51708389
#include <vector>

class Solution {
public:
    int strStr(string haystack, string needle) {
        int strinf_size  = (int) haystack.size();
        int pattern_size = (int) needle.size();

        // generate fail_array, takes O(n) time
        vector<int> fail_array(pattern_size, -1);
        int prefix_cursor_position  = -1;
        int pattern_cursor_position = 0;
        while (pattern_cursor_position < pattern_size - 1) {
            if (prefix_cursor_position == -1 || needle[prefix_cursor_position] == needle[pattern_cursor_position]) {
                prefix_cursor_position  += 1;
                pattern_cursor_position += 1;
                fail_array[pattern_cursor_position] = prefix_cursor_position;
            } else {
                // back to previous position to find prefix for next element
                prefix_cursor_position = fail_array[prefix_cursor_position];
            }
        }

        // check through the haystack using fail_array, takes O(m) time
        int string_cursor_position = 0;
        pattern_cursor_position = 0;
        while (string_cursor_position < strinf_size && pattern_cursor_position < pattern_size) {
            if (pattern_cursor_position == -1 || haystack[string_cursor_position] == needle[pattern_cursor_position]) {
                string_cursor_position  += 1;
                pattern_cursor_position += 1;
            } else {
                pattern_cursor_position = fail_array[pattern_cursor_position];
            }
        }
        return (pattern_cursor_position == pattern_size) ? (string_cursor_position - pattern_cursor_position) : -1;
    }
};
