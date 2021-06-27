// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := ratings.size()
// Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
#include <numeric>

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 1);

        for (int index = 1; index < ratings.size(); ++index)
            if (ratings[index] > ratings[index - 1] && candies[index] <= candies[index - 1])
                candies[index] = candies[index - 1] + 1;
        for (int index = ratings.size() - 2; index >= 0; --index)
            if (ratings[index] > ratings[index + 1] && candies[index] <= candies[index + 1])
                candies[index] = candies[index + 1] + 1;
        return accumulate(candies.begin(), candies.end(), 0);
    }
};
