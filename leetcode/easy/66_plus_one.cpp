// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := digits.size()
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for (int index = digits.size() - 1; index >= 0; --index) {
            if (carry == 0)
                break;

            int curr_num = digits[index];
            digits[index] = (curr_num + carry) % 10;
            carry = (curr_num + carry) / 10;
        }
        if (carry > 0)
            digits.insert(digits.begin(), carry);

        return digits;
    }
};
