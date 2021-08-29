// -----------------------------------------
// Model Solution: Greedy
//
// Time  Complexity: O(m + log2(n))
// Space Complexity: O(1)
// -----------------------------------------
// m := nums.size()
//
// Ref: https://leetcode.com/problems/patching-array/discuss/1432422/Python-2-solutions%3A-merge-intervals-%2B-greedy-explained

class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long covered_range_upper = 0;
        int min_patches_required = 0;
        int index = 0;
        while (covered_range_upper < n) {
            if (index < nums.size() && nums[index] <= covered_range_upper + 1) {
                covered_range_upper += nums[index];
                ++index;
            } else {
                ++min_patches_required;
                covered_range_upper = 2 * covered_range_upper + 1;
            }
        }

        return min_patches_required;
    }
};
