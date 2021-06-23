// -----------------------------------------
// My Solution: Hash Map
//
// Time  Complexity: O(m + n)
// Space Complexity: O(m + n)
// -----------------------------------------
// m := nums1.size(), n := nums2.size()
#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> intersections;

        for (auto num : nums1) nums_1_counter[num] += 1;
        for (auto num : nums2) {
            if (nums_1_counter[num] > 0) {
                intersections.push_back(num);
                --nums_1_counter[num];
            }
        }
        return intersections;
    }

private:
    unordered_map<int, int> nums_1_counter;
};

// -----------------------------------------
// Model Solution: Sort
//
// Time  Complexity: O(mlog(m) + nlog(n))
// Space Complexity: O(m + n)
// -----------------------------------------
// m := nums1.size(), n := nums2.size()
// Ref: https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82263/C%2B%2B-hash-table-solution-and-sort-%2B-two-pointers-solution-with-time-and-space-complexity
#include <algorithm>
#include <vector>

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> intersections;
        int nums_1_pointer = 0, nums_2_pointer = 0;

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        while (nums_1_pointer < nums1.size() && nums_2_pointer < nums2.size()) {
            if (nums1[nums_1_pointer] == nums2[nums_2_pointer]) {
                intersections.push_back(nums1[nums_1_pointer]);
                ++nums_1_pointer;
                ++nums_2_pointer;
            } else if (nums1[nums_1_pointer] < nums2[nums_2_pointer]) {
                ++nums_1_pointer;
            } else {
                ++nums_2_pointer;
            }
        }
        return intersections;
    }
};
