// -----------------------------------------
// My Solution
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(1)
// -----------------------------------------
class Solution {
public:
    int trailingZeroes(int n) {
        int two_count = 0, five_count = 0;
        for (int curr_num = 1; curr_num <= n; ++curr_num) {
            int num = curr_num;
            while (num % 2 == 0) {
                two_count += 1;
                num /= 2;
            }
            while (num % 5 == 0) {
                five_count += 1;
                num /= 5;
            }
        }

        return min(two_count, five_count);
    }
};

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(log(n))
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52373/Simple-CC%2B%2B-Solution-(with-detailed-explaination)
class Solution {
public:
    int trailingZeroes(int n) {
        int zeroes_count = 0;
        while (n > 0) {
            zeroes_count += n / 5;
            n /= 5;
        }

        return zeroes_count;
    }
};
