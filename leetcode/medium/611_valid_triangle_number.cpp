// -----------------------------------------
// My Solution: Binary Search
//
// Time  complexity: O((n^2) * log2(n))
// Space Complexity: O(log2(n))
// -----------------------------------------
// n := nums.size()
//
// Note: log2(n) is the space complexity for sorting
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        if (nums.size() < 3)
            return 0;

        sort(nums.begin(), nums.end());

        int triangle_triplets_count = 0;
        for (int num_1_index = 0; num_1_index < nums.size() - 2; ++num_1_index) {
            for (int num_2_index = num_1_index + 1; num_2_index < nums.size() - 1; ++num_2_index) {
                int largest_num_3_index = lower_bound(nums.begin() + num_2_index + 1, nums.end(), nums[num_1_index] + nums[num_2_index]) - nums.begin() - 1;
                triangle_triplets_count += largest_num_3_index - num_2_index;
            }
        }
        return triangle_triplets_count;
    }
};

// -----------------------------------------
// My Solution: Two Pointers
//
// Time  complexity: O(n^2)
// Space Complexity: O(log2(n))
// -----------------------------------------
// n := nums.size()
//
// Ref:  https://leetcode.com/problems/valid-triangle-number/discuss/1339340/C%2B%2BPython-Two-Pointers-Picture-Explain-Clean-and-Concise-O(N2)
// Note: log2(n) is the space complexity for sorting
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int triangle_triplets_count = 0;
        for (int k = 2; k < nums.size(); ++k) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {
                    triangle_triplets_count += j - i;
                    j -= 1;
                } else {
                    i += 1;
                }
            }
        }

        return triangle_triplets_count;
    }
};
