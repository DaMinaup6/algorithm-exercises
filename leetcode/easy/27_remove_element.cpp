// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left_cursor_position  = 0;
        int right_cursor_position = nums.size() - 1;
        while (left_cursor_position <= right_cursor_position) {
            while (right_cursor_position >= left_cursor_position && nums[right_cursor_position] == val) {
                right_cursor_position -= 1;
            }
            if (right_cursor_position < left_cursor_position)
                break;

            if (nums[left_cursor_position] == val)
                swap(nums[left_cursor_position], nums[right_cursor_position]);
            left_cursor_position += 1;
        }

        return left_cursor_position;
    }
};
