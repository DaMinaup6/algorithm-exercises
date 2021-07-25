// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(log2(n))
// Space Complexity: O(log2(n))
// -----------------------------------------
//
// Ref: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/103766/C%2B%2B-4-lines-DPFibonacci-6-ms
class Solution {
public:
    int findIntegers(int n) {
        if (n < 3)
            return n + 1;
        if (n == 3)
            return 3;

        vector<int> power_2_minus_1_no_consecutive_ones_count = {2, 3};
        for (int bit = 3; bit <= 30; ++bit) {
            if (1 << (bit - 1) > n)
                break;
            int last_count = power_2_minus_1_no_consecutive_ones_count.back();
            int prev_count = power_2_minus_1_no_consecutive_ones_count[power_2_minus_1_no_consecutive_ones_count.size() - 2];
            power_2_minus_1_no_consecutive_ones_count.push_back(prev_count + last_count);
        }

        for (int bit_index = power_2_minus_1_no_consecutive_ones_count.size() - 1; bit_index > 1; --bit_index) {
            // check binary representation of n starts with "11" or "10"
            // starts with "11" -> return power_2_minus_1_no_consecutive_ones_count[bit_index]
            // starts with "10" -> return power_2_minus_1_no_consecutive_ones_count[bit_index - 1] + findIntegers(n & ~(1 << bit_index))
            if ((n & (1 << bit_index)) != 0)
                return (n & (1 << (bit_index - 1))) != 0 ? power_2_minus_1_no_consecutive_ones_count[bit_index] : power_2_minus_1_no_consecutive_ones_count[bit_index - 1] + findIntegers(n & ~(1 << bit_index));
        }
        return 0;
    }
};
