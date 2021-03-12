# -----------------------------------------
# My Solution
#
# Time  Complexity: O(m^2)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(s), n := len(wordDict)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False for _ in range(len(s))]
        for s_index in range(len(s)):
            sub_s = s[:(s_index + 1)]

            if sub_s in word_set:
                dp[s_index] = True
            else:
                for dp_index in range(s_index - 1, -1, -1):
                    if dp[dp_index] == True and s[(dp_index + 1):(s_index + 1)] in word_set:
                        dp[s_index] = True
                        break

        return dp[len(s) - 1]
