// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(mn)
// Space Complexity: O(m + n)
// -----------------------------------------
// m := num1.length(), n := num2.length()
// Ref: https://leetcode.com/problems/multiply-strings/discuss/1208875/C%2B%2B-or-0ms-or-100-faster-or-Very-simple
class Solution {
public:
    string multiply(string num1, string num2) {
        int num1_length = num1.length();
        int num2_length = num2.length();

        string result(num1_length + num2_length, '0');
        for (int num1_index = num1_length - 1; num1_index >= 0; --num1_index) {
            for (int num2_index = num2_length - 1; num2_index >= 0; --num2_index) {
                int curr_digit = num1_index + num2_index + 1;
                int next_digit = num1_index + num2_index;

                int curr_multiply = (num1[num1_index] - '0') * (num2[num2_index] - '0');
                int curr_sum = curr_multiply + (result[curr_digit] - '0');
                result[curr_digit] = (curr_sum % 10) + '0';
                result[next_digit] += curr_sum / 10; // add carry to next digit
            }
        }

        size_t non_zero_position = result.find_first_not_of("0");
        return non_zero_position != string::npos ? result.substr(non_zero_position) : "0";
    }
};
