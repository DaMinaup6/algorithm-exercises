// -----------------------------------------
// My Solution
//
// Time  Complexity: O(m + n)
// Space Complexity: O(m + n)
// -----------------------------------------
// m := pattern.size(), n := s.size()
#include <unordered_map>

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        // make sure we will consider all words in s since we get last complete word by reaching blank
        s += ' ';

        int pattern_type = 0, word_type = 0;
        int pattern_pointer_position = 0;
        int s_pointer_position = 0;
        while (pattern_pointer_position < pattern.size() && s_pointer_position < s.size()) {
            string word = "";
            while (s[s_pointer_position] != ' ') {
                word += s[s_pointer_position];
                ++s_pointer_position;
            }

            char pattern_char = pattern[pattern_pointer_position];
            if (pattern_type_mapping.find(pattern_char) == pattern_type_mapping.end()) {
                pattern_type_mapping[pattern_char] = pattern_type;
                ++pattern_type;
            }
            if (word_type_mapping.find(word) == word_type_mapping.end()) {
                word_type_mapping[word] = word_type;
                ++word_type;
            }
            if (pattern_type_mapping[pattern_char] != word_type_mapping[word])
                return false;

            ++pattern_pointer_position;
            ++s_pointer_position;
        }

        return pattern_pointer_position == pattern.size() && s_pointer_position == s.size();
    }

private:
    unordered_map<char, int> pattern_type_mapping;
    unordered_map<string, int> word_type_mapping;
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(m + n)
// Space Complexity: O(m + n)
// -----------------------------------------
// m := pattern.size(), n := s.size()
// Ref: https://leetcode.com/problems/word-pattern/discuss/73434/0ms-C%2B%2B-solution-using-istringstream-and-double-maps
#include <sstream>
#include <unordered_map>

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        istringstream string_stream(s);
        string word;

        int pattern_pointer_position = 0;
        int pattern_type = 1, word_type = 1;
        while (string_stream >> word) {
            if (pattern_pointer_position == pattern.size())
                return false;

            char pattern_char = pattern[pattern_pointer_position];
            if (pattern_type_mapping[pattern_char] == 0) {
                pattern_type_mapping[pattern_char] = pattern_type;
                ++pattern_type;
            }
            if (word_type_mapping[word] == 0) {
                word_type_mapping[word] = word_type;
                ++word_type;
            }
            if (word_type_mapping[word] != pattern_type_mapping[pattern_char])
                return false;

            ++pattern_pointer_position;
        }

        return pattern_pointer_position == pattern.size();
    }

private:
    unordered_map<char, int> pattern_type_mapping;
    unordered_map<string, int> word_type_mapping;
};
