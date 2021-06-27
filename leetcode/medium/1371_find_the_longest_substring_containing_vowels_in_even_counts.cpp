// -----------------------------------------
// My Solution: Bitmask
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()
// Note: This problem is related to problem 1915
class Solution {
public:
    int findTheLongestSubstring(string s) {
        static unordered_map<char, int> vowel_bit_map = {{'a', 0}, {'e', 1}, {'i', 2}, {'o', 3}, {'u', 4}};
        unordered_map<int, int> mask_prev_index = {{0, -1}};
        int mask = 0;

        // if same mask encountered during for loop, it means substring between two masks contains vowels with even count only
        // e.g. "a" and "aaaee" have same mask, so subtring "aaee" between them contains vowels with even count only
        int longest_substring_length = 0;
        for (int index = 0; index < s.size(); ++index) {
            char curr_char = s[index];
            if (vowel_bit_map.find(curr_char) != vowel_bit_map.end())
                mask ^= 1 << vowel_bit_map[curr_char];

            if (mask_prev_index.find(mask) == mask_prev_index.end()) {
                mask_prev_index[mask] = index;
            } else {
                longest_substring_length = max(longest_substring_length, index - mask_prev_index[mask]);
            }
        }
        return longest_substring_length;
    }
};
