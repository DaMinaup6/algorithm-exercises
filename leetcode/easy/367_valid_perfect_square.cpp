// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(sqrt(n))
// Space Complexity: O(1)
// -----------------------------------------
// n := num
// Ref: https://leetcode.com/problems/valid-perfect-square/discuss/622060/Unique-solution-Easy-to-understand.-C%2B%2B
class Solution {
public:
    bool isPerfectSquare(int num) {
        //  1 == 1
        //  4 == 1 + 3
        //  9 == 1 + 3 + 5
        // 16 == 1 + 3 + 5 + 7
        // ...
        int curr_odd_num = 1;

        while (num > 0) {
            num -= curr_odd_num;
            curr_odd_num += 2;
        }
        return num == 0;
    }
};

// -----------------------------------------
// Model Solution: Binary Search
//
// Time  Complexity: O(log(n))
// Space Complexity: O(1)
// -----------------------------------------
// n := num
// Ref: https://leetcode.com/problems/valid-perfect-square/discuss/83888/O(logN)-Bisection-method
class Solution {
public:
    bool isPerfectSquare(int num) {
        long long left_cursor = 0, right_cursor = num;
        while (left_cursor <= right_cursor) {
            long long mid_cursor = (left_cursor + right_cursor) / 2;
            long long mid_square = pow(mid_cursor, 2);

            if (mid_square == num)
                return true;
            else if (mid_square > num)
                right_cursor = mid_cursor - 1;
            else
                left_cursor = mid_cursor + 1;
        }
        return false;
    }
};
