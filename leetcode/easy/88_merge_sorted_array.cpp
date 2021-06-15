// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(m + n)
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/merge-sorted-array/discuss/1191368/C%2B%2B%3A-0ms-faster-than-100-of-C%2B%2B
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int nums1_cursor_position = m - 1, nums2_cursor_position = n - 1;
        for (int index = m + n - 1; index >= 0; --index) {
            if (nums2_cursor_position < 0)
                break;

            if (nums1_cursor_position >= 0 && nums1[nums1_cursor_position] > nums2[nums2_cursor_position]) {
                nums1[index] = nums1[nums1_cursor_position];
                --nums1_cursor_position;
            } else {
                nums1[index] = nums2[nums2_cursor_position];
                --nums2_cursor_position;
            }
        }
    }
};
