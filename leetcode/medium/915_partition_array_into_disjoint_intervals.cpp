// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int nums_size = nums.size();

        vector<int> min_from_right(nums_size);
        min_from_right[nums_size - 1] = nums.back();
        for (int index = nums_size - 2; index >= 0; --index)
            min_from_right[index] = min(min_from_right[index + 1], nums[index]);

        int curr_max = INT_MIN;
        for (int index = 0; index < nums_size - 1; ++index) {
            curr_max = max(curr_max, nums[index]);
            if (curr_max <= min_from_right[index + 1])
                return index + 1;
        }
        return nums_size;
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
//
// Ref: https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/1354396/Python-From-O(N)-space-to-O(1)-space-Clean-and-Concise
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int local_max  = nums[0];
        int global_max = nums[0];
        int partition  = 0;
        for (int index = 1; index < nums.size(); ++index) {
            global_max = max(global_max, nums[index]);
            // the last index such that nums[index] < local_max is the partition index
            if (nums[index] < local_max) {
                partition = index;
                local_max = global_max;
            }
        }

        return partition + 1;
    }
};
