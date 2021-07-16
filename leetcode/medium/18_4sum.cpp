// -----------------------------------------
// Model Solution: Two Pointers
//
// Time  Complexity: O(n^2)
// Space Complexity: O(log2(n))
// -----------------------------------------
// n := nums.size()
//
// Ref:  https://leetcode.com/problems/4sum/discuss/1341213/C%2B%2BPython-2-solutons-Clean-and-Concise-Follow-up-questions
// Note: Extra Space (without count output as space): O(log2(n)), for sorting space.
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4)
            return {};
        sort(nums.begin(), nums.end());
        if (4 * nums[0] > target || 4 * nums.back() < target)
            return {};

        vector<vector<int>> quadruplets;

        int num_1_index = 0;
        while (num_1_index < nums.size()) {

            int num_2_index = num_1_index + 1;
            while (num_2_index < nums.size()) {
                int num_3_index = num_2_index + 1, num_4_index = nums.size() - 1;
                int target_remain = target - nums[num_1_index] - nums[num_2_index];
                while (num_3_index < num_4_index) {
                    if (nums[num_3_index] + nums[num_4_index] == target_remain) {
                        quadruplets.push_back({nums[num_1_index], nums[num_2_index], nums[num_3_index], nums[num_4_index]});

                        skip_duplicate_numbers(nums, num_3_index);
                        ++num_3_index;
                        skip_duplicate_numbers(nums, num_4_index, -1);
                        --num_4_index;
                    } else if (nums[num_3_index] + nums[num_4_index] > target_remain) {
                        --num_4_index;
                    } else {
                        ++num_3_index;
                    }
                }

                skip_duplicate_numbers(nums, num_2_index);
                ++num_2_index;
            }

            skip_duplicate_numbers(nums, num_1_index);
            ++num_1_index;
        }

        return quadruplets;
    }

private:
    void skip_duplicate_numbers(vector<int>& nums, int& num_index, int move = 1) {
        while (num_index + move >= 0 && num_index + move < nums.size() && nums[num_index] == nums[num_index + move])
            num_index += move;
    }
};

