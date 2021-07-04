// -----------------------------------------
// Model Solution: Binary Search + Rabin-Karp's Rolling Hash
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := s.length()
//
// Ref: https://leetcode.com/problems/longest-duplicate-substring/discuss/695965/C%2B%2B-Using-Binary-Search-%2B-Rabin-Karp's-Rolling-Hash
class Solution {
public:
    string longestDupSubstring(string s) {
        string longest_duplicated_string = "";

        int min_possible_duplicated_length = 1;
        int max_possible_duplicated_length = s.length() - 1;
        while (min_possible_duplicated_length <= max_possible_duplicated_length) {
            int target_duplicated_length = (min_possible_duplicated_length + max_possible_duplicated_length) / 2;

            string curr_duplicated_string = get_duplicated_string_with_length(s, target_duplicated_length);
            if (curr_duplicated_string.empty()) {
                max_possible_duplicated_length = target_duplicated_length - 1;
            } else {
                min_possible_duplicated_length = target_duplicated_length + 1;
                longest_duplicated_string = curr_duplicated_string;
            }
        }
        return longest_duplicated_string;
    }

    // Introduction to Rolling Hash: https://www.youtube.com/watch?v=BfUejqd07yo
    string get_duplicated_string_with_length(string& whole_string, int target_duplicated_length) {
        unordered_set<long long> seen_hash_values;

        long long curr_power = 1;
        long long hash_value = (whole_string[target_duplicated_length - 1] - 'a');
        for (int index = 1; index < target_duplicated_length; ++index) {
            curr_power = (curr_power * 26) % MOD;
            hash_value = (hash_value + ((whole_string[target_duplicated_length - 1 - index] - 'a') * curr_power) % MOD) % MOD;
        }
        seen_hash_values.insert(hash_value);

        for (int index = 1; index <= whole_string.length() - target_duplicated_length; ++index) {
            // Modular Subtraction: https://youtu.be/-OPohCQqi_E?t=462
            hash_value = (hash_value - ((whole_string[index - 1] - 'a') * curr_power) % MOD + MOD) % MOD;
            hash_value = (hash_value * 26) % MOD;
            hash_value = (hash_value + (whole_string[index + target_duplicated_length - 1] - 'a')) % MOD;

            if (seen_hash_values.find(hash_value) != seen_hash_values.end())
                return whole_string.substr(index, target_duplicated_length);
            seen_hash_values.insert(hash_value);
        }
        return "";
    }

private:
    // should select a huge enough modular number, this modular number comes from following reference
    // Ref: https://leetcode.com/problems/longest-common-subpath/discuss/1314826/Rolling-Hash-%2B-Collision-Check
    static const long long MOD = 100000000019;
};
