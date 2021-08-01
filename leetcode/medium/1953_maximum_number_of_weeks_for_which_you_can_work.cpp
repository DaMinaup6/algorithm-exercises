// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := milestones.size()
//
// Ref: https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-in-O(n)-with-detailed-explanation-and-common-failure-analysis
class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        // If there are at least two projects with same number of milestones and
        // there isn't a project with more milestones than that two, we can finish all milestones.
        long long milestones_sum = accumulate(milestones.begin(), milestones.end(), 0ll);
        long long max_milestone  = *max_element(milestones.begin(), milestones.end());

        if (milestones_sum - max_milestone >= max_milestone)
            return milestones_sum;
        return 2 * (milestones_sum - max_milestone) + 1;
    }
};
