// -----------------------------------------
// Model Solution: Dynamic Programming
//
// Time Complexity: O(n)
// -----------------------------------------
// n := s.size()
//
// Ref: https://leetcode.com/problems/decode-ways-ii/solution/

// -----> Version 1: Space Complexity: O(n)
class Solution {
public:
    int numDecodings(string s) {
        vector<long> dp(s.size() + 1);

        dp[0] = 1;
        dp[1] = s[0] == '*' ? 9 : (s[0] == '0' ? 0 : 1);
        for (int index = 1; index < s.size(); ++index) {
            if (s[index] == '*') {
                // consider s[index] as number to decode
                dp[index + 1] = 9 * dp[index] % MOD;
                // consider (s[(index - 1)] + s[index]) as number to decode
                if (s[index - 1] == '1')
                    dp[index + 1] = (dp[index + 1] + 9 * dp[index - 1]) % MOD;
                else if (s[index - 1] == '2')
                    dp[index + 1] = (dp[index + 1] + 6 * dp[index - 1]) % MOD;
                else if (s[index - 1] == '*')
                    dp[index + 1] = (dp[index + 1] + 15 * dp[index - 1]) % MOD;
            } else {
                // consider s[index] as number to decode
                dp[index + 1] = s[index] != '0' ? dp[index] : 0;
                // consider (s[(index - 1)] + s[index]) as number to decode
                if (s[index - 1] == '1' || s[index - 1] == '2' && s[index] <= '6')
                    dp[index + 1] = (dp[index + 1] + dp[index - 1]) % MOD;
                else if (s[index - 1] == '*')
                    dp[index + 1] = (dp[index + 1] + (s[index] <= '6' ? 2 : 1) * dp[index - 1]) % MOD;
            }

            if (dp[index + 1] == 0)
                return 0;
        }

        return dp.back();
    }

private:
    static const int MOD = 1e9 + 7;
};

// -----> Version 2: Space Complexity: O(1)
class Solution {
public:
    int numDecodings(string s) {
        long prev_dp = 1, curr_dp, next_dp;

        curr_dp = s[0] == '*' ? 9 : (s[0] == '0' ? 0 : 1);
        for (int index = 1; index < s.size(); ++index) {
            if (s[index] == '*') {
                next_dp = 9 * curr_dp % MOD;
                if (s[index - 1] == '1')
                    next_dp = (next_dp + 9 * prev_dp) % MOD;
                else if (s[index - 1] == '2')
                    next_dp = (next_dp + 6 * prev_dp) % MOD;
                else if (s[index - 1] == '*')
                    next_dp = (next_dp + 15 * prev_dp) % MOD;
            } else {
                next_dp = s[index] != '0' ? curr_dp : 0;
                if (s[index - 1] == '1' || s[index - 1] == '2' && s[index] <= '6')
                    next_dp = (next_dp + prev_dp) % MOD;
                else if (s[index - 1] == '*')
                    next_dp = (next_dp + (s[index] <= '6' ? 2 : 1) * prev_dp) % MOD;
            }

            prev_dp = curr_dp;
            curr_dp = next_dp;
            if (curr_dp == 0)
                return 0;
        }

        return curr_dp;
    }

private:
    static const int MOD = 1e9 + 7;
};
