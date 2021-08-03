// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n * 2^n)
// Space Complexity: O(2^n)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        for (int& num: nums)
            ++nums_counter[num];

        for (auto& key_value : nums_counter)
            unique_nums.push_back(key_value.first);

        vector<int> nums_count_arr;
        generate_subsets(nums_count_arr);
        return all_subsets;
    }

private:
    unordered_map<int, int> nums_counter;
    vector<int> unique_nums;
    vector<vector<int>> all_subsets;

    void generate_subsets(vector<int>& nums_count_arr) {
        if (nums_count_arr.size() == unique_nums.size()) {
            vector<int> subset;
            for (int index = 0; index < nums_count_arr.size(); ++index)
                for (int counter = 0; counter < nums_count_arr[index]; ++counter)
                    subset.push_back(unique_nums[index]);

            all_subsets.push_back(subset);
            return;
        }

        int curr_num = unique_nums[nums_count_arr.size()];
        for (int num_count = 0; num_count <= nums_counter[curr_num]; ++num_count) {
            nums_count_arr.push_back(num_count);
            generate_subsets(nums_count_arr);
            nums_count_arr.pop_back();
        }
    }
};
