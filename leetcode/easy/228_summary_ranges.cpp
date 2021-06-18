// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := points.size()
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ranges = {};
        int range_start_index = 0, range_end_index = 0;
        int index = 0;
        while (index < nums.size()) {
            // don't use nums[index + 1] - nums[range_start_index] == (index + 1) - range_start_index as consition here
            // since -2^(31) <= nums[i] <= 2^(31) - 1
            // we get signed integer overflow if nums == [-2147483648, -2147483647, 2147483647] here
            while (index + 1 < nums.size() && nums[index + 1] == nums[index] + 1) {
                ++index;
                range_end_index = index;
            }

            if (range_start_index == range_end_index) {
                ranges.push_back(to_string(nums[range_start_index]));
            } else {
                ranges.push_back(to_string(nums[range_start_index]) + "->" + to_string(nums[range_end_index]));
            }

            ++index;
            range_start_index = range_end_index = index;
        }

        return ranges;
    }
};
