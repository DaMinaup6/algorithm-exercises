// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(k)
// -----------------------------------------
// n := nums.size()
#include <unordered_set>

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0)
            return false;

        unordered_set<int> stored_nums;
        for (int index = 0; index < nums.size(); ++index) {
            if (stored_nums.find(nums[index]) != stored_nums.end())
                return true;

            stored_nums.insert(nums[index]);
            if (stored_nums.size() == k + 1) {
                stored_nums.erase(nums[index - k]);
            }
        }
        return false;
    }
};
