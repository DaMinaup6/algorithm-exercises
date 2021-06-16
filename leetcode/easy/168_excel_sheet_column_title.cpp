// -----------------------------------------
// My Solution
//
// Time  Complexity: O(log(n))
// Space Complexity: O(log(n))
// -----------------------------------------
// n := columnNumber
// Ref: https://www.youtube.com/watch?v=f7JOBJIC-NA
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string title = "";

        while (columnNumber > 0) {
            int remain_num = columnNumber % 26;
            if (remain_num == 0)
                remain_num = 26;
            title = (char) ('A' - 1 + remain_num) + title;

            columnNumber = (columnNumber - remain_num) / 26;
        };
        return title;
    }
};
