// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := prices.size()
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curr_buy_price = prices[0];
        int total_profit = 0;
        for (int index = 1; index < prices.size(); ++index) {
            if (prices[index] < curr_buy_price) {
                curr_buy_price = prices[index];
            } else {
                total_profit += prices[index] - curr_buy_price;
                curr_buy_price = prices[index];
            }
        }
        return total_profit;
    }
};
