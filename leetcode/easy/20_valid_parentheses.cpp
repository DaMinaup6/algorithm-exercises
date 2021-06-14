// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n)
// Space Complexity: O(n)
// -----------------------------------------
// n := s.size()
class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (int index = 0; index < s.size(); ++index) {
            if (s[index] == '(' || s[index] == '[' || s[index] == '{') {
                stack.push_back(s[index]);
            } else {
                if (stack.size() == 0)
                    return false;
                if (s[index] == ')' && stack.back() != '(' || s[index] == ']' && stack.back() != '[' || s[index] == '}' && stack.back() != '{')
                    return false;
                stack.pop_back();
            }
        }

        return stack.size() == 0;
    }
};
