# -----------------------------------------
# Dynamic Programming
# -----------------------------------------
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        # dp[i] := valid length from s[0] to s[i]
        dp = [0] * len(s)
        dp[1] = 2 if s[:2] == '()' else 0

        max_len = max(dp[:2])
        for char_idx in range(2, len(s)):
            char = s[char_idx]
            if char == ')':
                if s[char_idx - 1] == '(':
                    dp[char_idx] = dp[char_idx - 2] + 2
                elif s[char_idx - 1] == ')' and char_idx - dp[char_idx - 1] - 1 >= 0 and s[char_idx - dp[char_idx - 1] - 1] == '(':
                    # e.g. for ((())), when char_idx == 4, which is ((()')'), need to check if s[1], which is ('('())) is '(' to see if it's a valid close bracket
                    #      then, if it's a valid close bracket, need to check it's previous valid length. For example ()(()), for ()(()')' it's a valid close bracket,
                    #      but there is '()'(()) in front of it which is also valid so need to add the previous valid length, that would be like
                    #      ( ) ( ( ) )
                    #      0 2 0 0 2 6
                    #      here prev_count is the valid length before nested brackets, which is "()"(()) in this example
                    prev_count   = dp[char_idx - dp[char_idx - 1] - 2] if char_idx - dp[char_idx - 1] - 2 >= 0 else 0
                    dp[char_idx] = dp[char_idx - 1] + prev_count + 2
            max_len = max(max_len, dp[char_idx])
        return max_len

processor = Solution()
print(f"processor.longestValidParentheses('')       == 0: {processor.longestValidParentheses('') == 0}")
print(f"processor.longestValidParentheses('(()')    == 2: {processor.longestValidParentheses('(()') == 2}")
print(f"processor.longestValidParentheses(')()())') == 4: {processor.longestValidParentheses(')()())') == 4}")
print(f"processor.longestValidParentheses('((()))') == 6: {processor.longestValidParentheses('((()))') == 6}")
print(f"processor.longestValidParentheses('(()())') == 6: {processor.longestValidParentheses('(()())') == 6}")
print(f"processor.longestValidParentheses('((())(((((())))(((((((((((((()))') == 8: {processor.longestValidParentheses('((())(((((())))(((((((((((((()))') == 8}")
