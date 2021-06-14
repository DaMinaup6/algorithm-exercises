// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(log(x))
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/reverse-integer/solution/
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || x % 10 == 0 && x != 0)
            return false;

        int reversed_num = 0;
        while (x > reversed_num) {
            reversed_num = reversed_num * 10 + x % 10;
            x /= 10;
        }
        // When the length is an odd number, we can get rid of the middle digit by revertedNumber / 10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        // since the middle digit doesn't matter in palidrome (it will always equal to itself), we can simply get rid of it.
        return (x == reversed_num) || (x == reversed_num / 10);
    }
};
