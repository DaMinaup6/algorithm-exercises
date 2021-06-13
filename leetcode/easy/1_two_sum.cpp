// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, vector<int>> num_indexes;
        int num;
        for (int index = 0; index < nums.size(); ++index) {
            num = nums[index];
            num_indexes[num].push_back(index);
        }

        for (int index = 0; index < nums.size(); ++index) {
            num = nums[index];
            if (target - num == num) {
                if (num_indexes[num].size() >= 2) {
                    for (int position = 0; position < num_indexes[num].size(); ++position) {
                        if (num_indexes[num][position] != index) {
                            return {index, num_indexes[num][position]};
                        }
                    }
                }
            } else if (num_indexes.find(target - num) != num_indexes.end()) {
                return {index, num_indexes[target - num][0]};
            }
        }

        return {-1, -1};
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
// Ref: https://leetcode.com/problems/two-sum/discuss/577000/C%2B%2B-beats-99.81
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_indexes;
        for (int index = 0; index < (int) nums.size(); ++index) {
            if (num_indexes.find(nums[index]) != num_indexes.end()) {
                return {index, num_indexes[nums[index]]};
            } else {
                num_indexes.insert({target - nums[index], index});
            }
        }
        return {-1, -1};
    }
};
