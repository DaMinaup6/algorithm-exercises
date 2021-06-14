// -----------------------------------------
// My Solution
//
// Time  Complexity: O(log(n))
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left_cursor_position  = 0;
        int right_cursor_posision = nums.size() - 1;

        int middle_cursor_position;
        while (left_cursor_position <= right_cursor_posision) {
            middle_cursor_position = (left_cursor_position + right_cursor_posision) / 2;
            if (nums[middle_cursor_position] < target) {
                left_cursor_position = middle_cursor_position + 1;
            } else {
                right_cursor_posision = middle_cursor_position - 1;
            }
        }
        return right_cursor_posision + 1;
    }
};
