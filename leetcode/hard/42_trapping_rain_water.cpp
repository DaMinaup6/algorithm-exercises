// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := height.size()
//
// Ref: https://leetcode.com/problems/trapping-rain-water/solution/
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2)
            return 0;

        int left_cursor = 0, right_cursor = height.size() - 1;
        int left_max_height = height[0], right_max_height = height.back();
        int trapped_water = 0;
        while (left_cursor < right_cursor) {
            if (left_max_height <= right_max_height) {
                trapped_water += left_max_height - height[left_cursor];
                ++left_cursor;
                left_max_height = max(left_max_height, height[left_cursor]);
            } else {
                trapped_water += right_max_height - height[right_cursor];
                --right_cursor;
                right_max_height = max(right_max_height, height[right_cursor]);
            }
        }
        return trapped_water;
    }
};
