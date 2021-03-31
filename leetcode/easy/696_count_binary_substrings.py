# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        consecutive_size = []
        curr_consecutive = 1
        s += '2'
        for index in range(1, len(s)):
            if s[index] == s[index - 1]:
                curr_consecutive += 1
            else:
                consecutive_size.append(curr_consecutive)
                curr_consecutive = 1
        if len(consecutive_size) == 1:
            return 0

        result = 0
        for index in range(1, len(consecutive_size)):
            result += min(consecutive_size[index], consecutive_size[index - 1])
        return result

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, ans = 0, 1, 0
        for index in range(1, len(s)):
            if s[index] == s[index - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            if prev >= curr:
                ans += 1
        return ans
