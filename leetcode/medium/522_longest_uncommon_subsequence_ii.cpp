// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(mn^2)
// Space Complexity: O(1)
// -----------------------------------------
// m := max length of strs[i], n := strs.size()
//
// Ref: https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/1428729/C%2B%2B-or-JAVA-or-Python3-2-Approaches-oror-Easy-to-Understand
class Solution {
public:
    bool check(string a, string b){
        int A = a.size();
        int B = b.size();

        while (A > 0 && B > 0) {
            int i = a.size() - A;
            int j = b.size() - B;
            if (a[i] == b[j])
                --A;
            --B;
        }
        return A == 0;
    }

    int findLUSlength(vector<string>& strs) {
        int maxLen = -1;
        for(int i = 0; i < strs.size(); ++i) {
            int currLen = strs[i].length();
            bool flag = true;
            for(int j = 0; j < strs.size(); ++j) {
                if (i != j && check(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }

            if (flag)
                maxLen = max(maxLen , currLen);
        }

        return maxLen;
    }
};
