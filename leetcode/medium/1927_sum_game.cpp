// -----------------------------------------
// My Solution: Math
//
// Time  Complexity: O(n)
// Space Complexity: O(1)
// -----------------------------------------
// n := num.size()
class Solution {
public:
    bool sumGame(string num) {
        int half_size = num.size() / 2;
        int sum_diff = 0;
        int question_mark_count_diff = 0;
        for (int index = 0; index < num.size(); ++index) {
            if (num[index] == '?')
                question_mark_count_diff += (index < half_size ? 1 : -1);
            else
                sum_diff += (index < half_size ? 1 : -1) * (num[index] - '0');
        }

        // In this case
        // * sum_diff == 0 => Bob just cancel all numbers choosen by Alcie => Bob wins
        // * sum_diff != 0 => no matter how many '?' are there, Alice can always cancel '?' choosen by Bob except first and last '?',
        //                    so Alice choose first '?' on the first half if sum_diff > 0 or first '?' on right side if sum_diff < 0 to be '9',
        //                    then Bob cannot make sum_diff to be zero since sum_diff now > 9 or < -9 => Alice wins
        if (question_mark_count_diff == 0)
            return sum_diff != 0;
        // If question_mark_count_diff is not multiples of 2 then can always ruin Bob's best strategy
        if (abs(question_mark_count_diff) % 2 != 0)
            return true;
        // e.g. If sum_diff == 54 and question_mark_count_diff == -12, there will be 6 numbers for Bob to choose on right half string
        //      Bob can always add -9 to sum_diff. For example Bob choose 5 if Alice choose 4, choose 0 if Alice choose 9.
        //      So sum_diff must be zero after all '?' filled.
        //      Otherwise Alice must wins.
        int abs_sum_diff = abs(sum_diff);
        int half_question_mark_count_diff = abs(question_mark_count_diff) / 2;
        if (question_mark_count_diff < 0 && (sum_diff <= 0 || abs_sum_diff % half_question_mark_count_diff != 0 || abs_sum_diff / half_question_mark_count_diff != 9))
            return true;
        if (question_mark_count_diff > 0 && (sum_diff >= 0 || abs_sum_diff % half_question_mark_count_diff != 0 || abs_sum_diff / half_question_mark_count_diff != 9))
            return true;
        return false;
    }
};
