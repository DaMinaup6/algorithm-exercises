// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(log(x))
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/reverse-integer/solution/
class Solution {
public:
    int reverse(int x) {
        int reversed_num = 0;
        int max_int_divide_10 = INT_MAX / 10;
        int min_int_divide_10 = INT_MIN / 10;

        while (x != 0) {
            // -12 % 10 == -2 in c++
            int pop = x % 10;

            x /= 10;
            // INT_MAX == 2147483647, so if reversed_num == INT_MAX / 10 and we need to add more than 7 it overflows
            if (reversed_num > max_int_divide_10 || (reversed_num == max_int_divide_10 && pop > 7)) return 0;
            // INT_MIN == -2147483648, so if reversed_num == INT_MIN / 10 and we need to add less than -8 it overflows
            if (reversed_num < min_int_divide_10 || (reversed_num == min_int_divide_10 && pop < -8)) return 0;
            reversed_num = reversed_num * 10 + pop;
        }
        return reversed_num;
    }
};
