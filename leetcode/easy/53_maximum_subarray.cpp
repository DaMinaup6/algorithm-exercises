// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum = 0;
        int max_sum  = INT_MIN;
        for (int index = 0; index < nums.size(); ++index) {
            curr_sum += nums[index];
            max_sum = max(max_sum, curr_sum);
            if (curr_sum < 0)
                curr_sum = 0;
        }

        return max_sum;
    }
};
