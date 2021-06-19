// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(log(n))
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/ugly-number/discuss/69353/Simple-C++-solution/294589
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0)
            return false;

        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        // check if n is power of 2 or not by considering (n & (n - 1)) == 0
        return (n & (n - 1)) == 0;
    }
};
