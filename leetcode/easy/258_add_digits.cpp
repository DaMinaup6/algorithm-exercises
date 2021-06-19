// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := to_string(num).size()
class Solution {
public:
    int addDigits(int num) {
        while (num >= 10) {
            string num_string = to_string(num);
            num = 0;
            for (int index = 0; index < num_string.size(); ++index) {
                num += ((int) num_string[index] - '0');
            }
        }
        return num;
    }
};

// -----------------------------------------
// Model Solution: Mathematical
//
// Time  Complexity: O(1)
// Space Complexity: O(1)
// -----------------------------------------
// Ref: https://leetcode.com/problems/add-digits/solution/
class Solution {
public:
    int addDigits(int num) {
        return num == 0 ? 0 : (1 + (num - 1) % 9);
    }
};
