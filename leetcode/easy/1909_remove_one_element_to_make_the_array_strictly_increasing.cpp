// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
// Ref: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1298586/C%2B%2B-%3A-O(n)-solution
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int i = 0;
        while (i < nums.size() - 1) {
            if (nums[i] >= nums[i + 1])
                break;
            ++i;
        }
        if (i == nums.size() - 1)
            return true;

        int j = nums.size() - 1;
        while (j > 0) {
            if (nums[j - 1] >= nums[j])
                break;
            --j;
        }

        // conditions:
        // a) position differ by 1 only
        // b) if nums[i] < nums[j + 1] => remove nums[j]
        // c) if nums[i - 1] < nums[j] => remove nums[i]
        //
        // otherwise it's not possible to make array strictly increasing with removing one element only
        return (j - i == 1) && (i == 0 || j == nums.size() - 1 || nums[i] < nums[j + 1] || nums[i - 1] < nums[j]);
    }
};
