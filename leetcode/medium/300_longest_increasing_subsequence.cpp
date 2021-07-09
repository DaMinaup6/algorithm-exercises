// -----------------------------------------
// My Solution: Patience Sort
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> longest_increasing_subsequence(1, nums[0]);
        for (int index = 1; index < nums.size(); ++index) {
            int insert_index = lower_bound(longest_increasing_subsequence.begin(), longest_increasing_subsequence.end(), nums[index]) - longest_increasing_subsequence.begin();
            if (insert_index == longest_increasing_subsequence.size())
                longest_increasing_subsequence.push_back(nums[index]);
            else
                longest_increasing_subsequence[insert_index] = nums[index];
        }

        return longest_increasing_subsequence.size();
    }
};
