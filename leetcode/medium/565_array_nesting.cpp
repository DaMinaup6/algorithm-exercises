// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := num.size()
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        unordered_set<int> checked_nums;

        size_t longest_length = 0;
        for (size_t index = 0; index < nums.size(); ++index) {
            unordered_map<int, size_t> collected_num_to_index_map;

            int collected_index = 0;
            int curr_num = nums[index];
            while (checked_nums.find(curr_num) == checked_nums.end()) {
                checked_nums.insert(curr_num);
                collected_num_to_index_map[curr_num] = collected_index;

                curr_num = nums[curr_num];
                ++collected_index;
            }

            if (collected_num_to_index_map.find(curr_num) != collected_num_to_index_map.end())
                longest_length = max(longest_length, collected_num_to_index_map.size() - collected_num_to_index_map[curr_num]);
        }

        return longest_length;
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := num.size()
//
// Ref: https://leetcode.com/problems/array-nesting/solution/
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int longest_length = 0;
        for (size_t index = 0; index < nums.size(); ++index) {
            int curr_num = nums[index];
            int curr_length = 0;
            while (curr_num >= 0 && nums[curr_num] >= 0) {
                int tmp   = curr_num;
                curr_num  = nums[curr_num];
                nums[tmp] = INT_MIN;

                ++curr_length;
            }

            longest_length = max(longest_length, curr_length);
        }

        return longest_length;
    }
};
