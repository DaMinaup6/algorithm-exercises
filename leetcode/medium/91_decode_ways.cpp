// -----------------------------------------
// My Solution: Dynamic Programming
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := s.size()
class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0')
            return 0;

        int dp_1 = 1, dp_2 = 1;
        for (size_t index = 1; index < s.size(); ++index) {
            int dp_3 = (s[index] != '0') ? dp_2 : 0;

            int two_digits_num = (s[index - 1] - '0') * 10 + (s[index] - '0');
            if (10 <= two_digits_num && two_digits_num <= 26)
                dp_3 += dp_1;

            if (dp_3 == 0)
                return 0;
            dp_1 = dp_2;
            dp_2 = dp_3;
        }

        return dp_2;
    }
};
