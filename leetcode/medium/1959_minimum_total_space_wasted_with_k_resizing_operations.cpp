// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(kn^2)
// Space Complexity: O(kn)
// -----------------------------------------
// n := nums.size()
//
// Ref: https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/discuss/1389247/C%2B%2BJavaPython-Simple-Top-down-DP-Clean-and-Concise

class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        nums_size = nums.size();
        min_space_wasted_cache = vector<vector<int>>(nums_size, vector<int>(k + 1, -1));

        return minSpaceWastedStartsFrom(nums, 0, k);
    }

private:
    int nums_size;
    vector<vector<int>> min_space_wasted_cache;

    int minSpaceWastedStartsFrom(vector<int>& nums, int start_index, int remain_resize_times) {
        if (start_index >= nums_size)
            return 0;
        if (remain_resize_times == -1)
            return 1e9;
        if (min_space_wasted_cache[start_index][remain_resize_times] > -1)
            return min_space_wasted_cache[start_index][remain_resize_times];

        int total_sum  = 0;
        int max_number = 0;
        int min_wasted = 1e9;
        for (int curr_index = start_index; curr_index < nums_size; ++curr_index) {
            total_sum += nums[curr_index];
            max_number = max(max_number, nums[curr_index]);
            min_wasted = min(min_wasted, (max_number * (curr_index - start_index + 1) - total_sum) + minSpaceWastedStartsFrom(nums, curr_index + 1, remain_resize_times - 1));
        }

        min_space_wasted_cache[start_index][remain_resize_times] = min_wasted;
        return min_wasted;
    }
};
