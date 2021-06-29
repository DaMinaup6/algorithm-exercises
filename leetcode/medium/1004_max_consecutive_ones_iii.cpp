// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int remain_flips = k;
        int consecutive_start = 0, consecutive_end = 0;
        int max_longest_ones  = 0;

        for (; consecutive_end < nums.size(); ++consecutive_end) {
            if (nums[consecutive_end] == 1) {
                max_longest_ones = max(max_longest_ones, consecutive_end - consecutive_start + 1);
            } else if (remain_flips > 0) {
                --remain_flips;
                max_longest_ones = max(max_longest_ones, consecutive_end - consecutive_start + 1);
            } else if (k == 0) {
                consecutive_start = consecutive_end + 1;
            } else {
                while (nums[consecutive_start] == 1)
                    ++consecutive_start;
                ++consecutive_start;
            }
        }
        return max_longest_ones;
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
// Ref: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/1305020/(C%2B%2B)-1004.-Max-Consecutive-Ones-III
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int zero_counter = 0;
        int consecutive_start = 0, consecutive_end = 0;
        int max_longest_ones  = 0;

        for (; consecutive_end < nums.size(); ++consecutive_end) {
            if (nums[consecutive_end] == 0)
                ++zero_counter;
            for (; zero_counter > k; ++consecutive_start) {
                if (nums[consecutive_start] == 0)
                    --zero_counter;
            }

            max_longest_ones = max(max_longest_ones, consecutive_end - consecutive_start + 1);
        }
        return max_longest_ones;
    }
};
