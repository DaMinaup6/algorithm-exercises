// -----------------------------------------
// My Solution: Dynamic Programming
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := nums.size()
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        long long max_odd_count_sum  = nums[0];
        long long max_even_count_sum = 0;
        // Strategy:
        // the answer must be max_odd_count_sum since max_even_count_sum must be smaller than max_odd_count_sum
        // if now we want to calculate max_odd_count_sum, it equals (max_even_count_sum + SOME_NUMBER)
        // so keep tracking max_odd_count_sum and max_even_count_sum then we get the answer
        //
        // e.g. nums == [6, 2, 1, 2, 4, 5] => max_odd_count_sum == 6 and max_even_count_sum == 0 after initialization
        //
        // At index 1: max_even_count_sum == max(0, 6 - 2) == 4, max_odd_count_sum == max(6, 4 + 2) == 6
        // At index 2: max_even_count_sum == max(4, 6 - 1) == 5, max_odd_count_sum == max(6, 5 + 1) == 6
        // At index 3: max_even_count_sum == max(5, 6 - 2) == 5, max_odd_count_sum == max(5, 5 + 2) == 7
        // At index 4: max_even_count_sum == max(5, 7 - 4) == 5, max_odd_count_sum == max(5, 5 + 4) == 9
        // At index 5: max_even_count_sum == max(5, 9 - 5) == 5, max_odd_count_sum == max(5, 5 + 5) == 10
        // so the answer is 10
        for (int index = 1; index < nums.size(); ++index) {
            max_even_count_sum = max(max_even_count_sum, max_odd_count_sum - nums[index]);
            max_odd_count_sum  = max(max_odd_count_sum, max_even_count_sum + nums[index]);
        }
        return max_odd_count_sum;
    }
};
