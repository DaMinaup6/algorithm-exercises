// -----------------------------------------
// My Solution: Binary Search + Rabin-Karp's Rolling Hash
//
// Time  Complexity: O((m + n) * log(min(m, n)))
// Space Complexity: O(m)
// -----------------------------------------
// m := nums1.size(), n := nums2.size()
class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        base = max(*max_element(nums1.begin(), nums1.end()), *max_element(nums2.begin(), nums2.end())) + 1;

        int min_common_length = 0;
        int max_common_length = min(nums1.size(), nums2.size());
        while (min_common_length <= max_common_length) {
            int target_common_length = (min_common_length + max_common_length) / 2;
            if (share_common_subarray(nums1, nums2, target_common_length))
                min_common_length = target_common_length + 1;
            else
                max_common_length = target_common_length - 1;
        }
        return max_common_length;
    }

    bool share_common_subarray(vector<int>& nums1, vector<int>& nums2, int target_common_length) {
        unordered_set<long> seen_subarray_values;
        long curr_power = 1;
        long subarray_value = 0;
        for (int index = 0; index < nums1.size(); ++index) {
            subarray_value = ((subarray_value * base) % MOD + nums1[index]) % MOD;
            if (index >= target_common_length)
                subarray_value = (subarray_value - (nums1[index - target_common_length] * curr_power) % MOD + MOD) % MOD;
            else
                curr_power = (curr_power * base) % MOD;

            if (index >= target_common_length - 1)
                seen_subarray_values.insert(subarray_value);
        }

        curr_power = 1;
        subarray_value = 0;
        for (int index = 0; index < nums2.size(); ++index) {
            subarray_value = ((subarray_value * base) % MOD + nums2[index]) % MOD;
            if (index >= target_common_length)
                subarray_value = (subarray_value - (nums2[index - target_common_length] * curr_power) % MOD + MOD) % MOD;
            else
                curr_power = (curr_power * base) % MOD;

            if (index >= target_common_length - 1 && seen_subarray_values.count(subarray_value) > 0)
                return true;
        }
        return false;
    }

private:
    static const int MOD = 1e9 + 7;
    int base;
};
