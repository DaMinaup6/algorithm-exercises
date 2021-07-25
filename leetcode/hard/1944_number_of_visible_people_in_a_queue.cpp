// -----------------------------------------
// Model Solution: Stack
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := heights.size()
//
// Ref: https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359707/JavaC%2B%2BPython-Stack-Solution-Next-Greater-Element
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        vector<int> right_people_seen(heights.size());
        vector<int> index_stack;
        for (int index = 0; index < heights.size(); ++index) {
            while (!index_stack.empty() && heights[index_stack.back()] <= heights[index]) {
                ++right_people_seen[index_stack.back()];
                index_stack.pop_back();
            }
            if (!index_stack.empty())
                ++right_people_seen[index_stack.back()];

            index_stack.push_back(index);
        }

        return right_people_seen;
    }
};
