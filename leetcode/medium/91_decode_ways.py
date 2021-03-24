# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
import math

class Solution:
    def numDecodings(self, s: str) -> int:
        valid_tens = set(['1', '2'])
        variations = []
        cursor = 0
        while cursor < len(s):
            if s[cursor] == '0' and (cursor == 0 or s[cursor - 1] not in valid_tens):
                return 0
            if s[cursor] not in valid_tens:
                cursor += 1
                continue

            variation = []
            while cursor < len(s) and s[cursor] in valid_tens:
                variation.append(s[cursor])
                cursor += 1
            if cursor < len(s):
                if s[cursor] == '0':
                    variation.pop()
                elif s[cursor] in ['3', '4', '5', '6'] or s[cursor] in ['7', '8', '9'] and s[cursor - 1] == '1':
                    variation.append(s[cursor])
            if len(variation) > 1:
                variations.append(variation)
            cursor += 1
        if len(variations) == 0:
            return 1

        result = 1
        for variation in variations:
            variation_num = 1
            for two_digits_num in range(1, len(variation) // 2 + 1):
                variation_num += math.comb(len(variation) - two_digits_num, two_digits_num)
            result *= variation_num

        return result

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82120874
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for index in range(1, len(s) + 1):
            if s[index - 1] != '0':
                dp[index] = dp[index - 1]
            # e.g. 222
            # 2:    [2]
            # 22:   [2, 2], [22] == ([2] + [2]) + ([] + [22])
            #                        dp[i - 1]  +  dp[i - 2]
            # 222:  [2, 2, 2], [22, 2], [2, 22] == ([2, 2] + [2]) + ([22] + [2]) + ([2] + [22])
            #                                                dp[i - 1]           +   dp[i - 2]
            if index > 1 and '10' <= s[(index - 2):index] <= '26':
                dp[index] += dp[index - 2]
            if dp[index] == 0:
                return 0

        return dp[-1]
