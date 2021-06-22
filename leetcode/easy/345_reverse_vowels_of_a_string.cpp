// -----------------------------------------
// My Solution: Two Pointers
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()
#include <unordered_set>

class Solution {
public:
    string reverseVowels(string s) {
        int left_pointer_position  = 0;
        int right_pointer_position = s.size() - 1;

        while (left_pointer_position < right_pointer_position) {
            while (left_pointer_position < right_pointer_position && !is_vowel(s[left_pointer_position]))
                left_pointer_position += 1;
            while (left_pointer_position < right_pointer_position && !is_vowel(s[right_pointer_position]))
                right_pointer_position -= 1;
            swap(s[left_pointer_position], s[right_pointer_position]);

            left_pointer_position  += 1;
            right_pointer_position -= 1;
        }
        return s;
    }

private:
    const unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    bool is_vowel(const char& character) const {
        return vowels.find(character) != vowels.end();
    }
};
