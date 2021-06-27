// -----------------------------------------
// Model Solution: Bitmask
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := word.size()
// Ref: https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299773/Intuitive-explanation-easy-to-understand
class Solution {
public:
    long long wonderfulSubstrings(string word) {
        // max value of mask is 1023 in this problem so set array size to 1024
        // set mask_counter[0] to be 1 so we are able to count single character as wonderful substring
        // e.g. word == "a", we have mask == (1)_2
        // in this case total_wonderful_strings should be 1 after first iteration
        // this can be achieved because we set mask_counter[0] to be 1
        // so it would be counted during the flip operations
        int mask_counter[1024] = {1};
        // e.g. for substring == "abc", we have mask === (111)_2; substring == "aac", we have mask === (100)_2
        // at bit i, 0 means the char in substring has even count, otherwise odd
        int mask = 0;

        // To calculate the answer, we go through from index 0 to the length of the string, updating the state of the string from [0...current index]
        // If we have seen our current state before, say [0...j] has the same state as [0...i], that means the substring between j and i has an even
        // count of all characters
        //
        // for example, mask of "aaa" equals mask of "a", which means from "a" to "aaa", we encounter substring with all chars have even count
        // this is true since in this case the substring between is "aa"
        // in this case, we add 1 to total_wonderful_strings
        // but if now substring is "aaaaa", we encounter same mask state twice, then we need to add 2 to total_wonderful_strings
        //
        // this is because, for example, string == "aabb" and we want to calculate number of substrings with all chars have even count
        // then the answer would be 3 since there are "aa", "bb" and "aabb"
        // so we add "how many times we encounter some mask state previously" to total_wonderful_strings each time we encounter same mask state
        //
        // At last, we are allowed to have one char with odd count in substring
        // so for every mask we try to flip one bit to see if it matches any state we've recorded before
        // if so then just add it to total_wonderful_strings
        long long total_wonderful_strings = 0;
        for (auto ch : word) {
            mask ^= 1 << (ch - 'a');
            total_wonderful_strings += mask_counter[mask];
            for (int bit = 0; bit < 10; ++bit)
                total_wonderful_strings += mask_counter[mask ^ (1 << bit)];

            ++mask_counter[mask];
        }
        return total_wonderful_strings;
    }
};
