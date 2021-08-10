// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int all_zeros_count = count(s.begin(), s.end(), '0');

        int curr_zeros_count = 0;
        int min_flips = s.size() - all_zeros_count;
        for (int index = 0; index < s.size(); ++index) {
            int ones_count_before_index = (index > 0) ? (index - curr_zeros_count) : 0;
            if (s[index] == '0')
                ++curr_zeros_count;
            int zeros_count_after_index = all_zeros_count - curr_zeros_count;
            // calculate how many flips needed if 1 starts from index in final string
            // flips == flip all 1 before index to 0 + flip 0 to 1 at index + flip all 0 after index to 1
            min_flips = min(min_flips, ones_count_before_index + (s[index] == '0') + zeros_count_after_index);
        }
        return min_flips;
    }
};
