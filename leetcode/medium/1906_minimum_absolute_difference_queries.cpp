// -----------------------------------------
// Model Solution: Bucket Sort
//
// Time  Complexity: O(m * (n + q))
// Space Complexity: O(mn)
// -----------------------------------------
// m := max num of nums, n := nums.size(), q := queries.size()
//
// Note: m is small in this problem so the time complexity is acceptable
//
// Ref:
// a) https://leetcode.com/problems/minimum-absolute-difference-queries/discuss/1284212/Python-Short-cumulative-sums-solution-explained
// b) https://leetcode.com/problems/minimum-absolute-difference-queries/discuss/1284472/C%2B%2B-Prefix-sum-with-counting-sort-thought-O(N-%2B-100-*-Queries)

#include <cmath>

class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        int max_num = *max_element(nums.begin(), nums.end());

        // e.g. if nums == [1, 1, 2], then we have
        //      buckets[0] == [0, 0, 0]
        //      buckets[1] == [0, 1, 0]
        //      buckets[2] == [0, 2, 0]
        //      buckets[3] == [0, 2, 1]
        vector<vector<int>> buckets(nums.size() + 1, vector<int>(max_num + 1, 0));
        for (int index = 1; index <= nums.size(); ++index) {
            buckets[index] = buckets[index - 1];
            buckets[index][nums[index - 1]] += 1;
        }

        vector<int> answers;
        for (int index = 0; index < queries.size(); ++index) {
            int start_index = queries[index][0];
            int end_index   = queries[index][1];
            int answer = -1;

            vector<int> sorted_sub_nums = get_sorted_sub_nums(buckets[start_index], buckets[end_index + 1]);
            for (int sub_index = 0; sub_index < sorted_sub_nums.size() - 1; ++sub_index) {
                int abs_diff = abs(sorted_sub_nums[sub_index] - sorted_sub_nums[sub_index + 1]);
                if (abs_diff > 0)
                    answer = (answer == -1) ? abs_diff : min(answer, abs_diff);
                if (answer == 1)
                    break;
            }
            answers.push_back(answer);
        }

        return answers;
    }

    vector<int> get_sorted_sub_nums(vector<int>& start_bucket, vector<int>& end_bucket) {
        vector<int> sorted_sub_nums;
        for (int index = 0; index < start_bucket.size(); ++index) {
            if (end_bucket[index] - start_bucket[index] > 0)
                sorted_sub_nums.push_back(index);
        }
        return sorted_sub_nums;
    }
};
