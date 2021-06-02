# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time Complexity: O(mn)
# -----------------------------------------
# m := len(word1), n := len(word2)

# -----> Version 1: Space Complexity: O(mn)
class Solution:
    def minDistance(self, word1, word2):
        # dp[i][j] := min edit distance of word1[0:i] and word2[0:j] for i > 0 and j > 0
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    if word1[i - 1] == word2[j - 1]:
                        # if word1[i - 1] == word2[j - 1], it means we can ignore current character and use previous result
                        # e.g. "ho" and "ro", then the edit distance equals to edit distance of "h" and "r"
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        # if word1[i - 1] != word2[j - 1], we have 3 options here, use dp[3][2] with "hor" and "ro" as example
                        #   a) remove last "r" of "hor" -> dp[i - 1][j]
                        #   b) remove last "o" of "ro"  -> dp[i][j - 1]
                        #   c) replace last "r" to "o"  -> dp[i - 1][j - 1], where use dp[i - 1][j - 1] because now last character equals
                        # chosee min edit distances of above 3 operations and plus 1 (since we either do remove or replace operation) as edit distance for dp[3][2]
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

# -----> Version 2: Space Complexity: O(n)
class Solution:
    def minDistance(self, word1, word2):
        curr_dp = [0] * (len(word2) + 1)

        for i in range(len(word1) + 1):
            next_dp = [0] * (len(word2) + 1)
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    next_dp[j] = max(i, j)
                else:
                    if word1[i - 1] == word2[j - 1]:
                        # if word1[i - 1] == word2[j - 1], it means we can ignore current character and use previous result
                        # e.g. "ho" and "ro", then the edit distance equals to edit distance of "h" and "r"
                        next_dp[j] = curr_dp[j - 1]
                    else:
                        # if word1[i - 1] != word2[j - 1], we have 3 options here, use dp[3][2] with "hor" and "ro" as example
                        #   a) remove last "r" of "hor" -> dp[i - 1][j]
                        #   b) remove last "o" of "ro"  -> dp[i][j - 1]
                        #   c) replace last "r" to "o"  -> dp[i - 1][j - 1], where use dp[i - 1][j - 1] because now last character equals
                        # chosee min edit distances of above 3 operations and plus 1 (since we either do remove or replace operation) as edit distance for dp[3][2]
                        next_dp[j] = min(curr_dp[j], next_dp[j - 1], curr_dp[j - 1]) + 1
            curr_dp = next_dp
        return curr_dp[-1]
