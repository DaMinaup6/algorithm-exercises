# -----------------------------------------
# My Solution
#
# Time  Complexity: O(math.comb(n, (n / 2)))
# Space Complexity: O(n)
# -----------------------------------------
# Note: This solution leads to TLE
import itertools

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) == k:
            return 0
        if k == 1:
            return self.to_palindrome_min_change(s)

        min_change = float('inf')
        for indexes in itertools.combinations(range(len(s)), k - 1):
            total_change = 0
            total_change += self.to_palindrome_min_change(s[:(indexes[0] + 1)])
            for index in range(1, len(indexes)):
                total_change += self.to_palindrome_min_change(s[(indexes[index - 1] + 1):(indexes[index] + 1)])
            total_change += self.to_palindrome_min_change(s[(indexes[-1] + 1):])

            min_change = min(min_change, total_change)

        return min_change

    def to_palindrome_min_change(self, s: str):
        if len(s) <= 1:
            return 0

        min_change = 0
        right_middle_index = len(s) // 2
        left_middle_index  = right_middle_index - 1 if len(s) % 2 == 0 else len(s) // 2
        radius = 0
        while left_middle_index - radius >= 0 and right_middle_index + radius < len(s):
            if s[left_middle_index - radius] != s[right_middle_index + radius]:
                min_change += 1
            radius += 1

        return min_change

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(kn^3)
# Space Complexity: O(kn)
# -----------------------------------------
# Ref: https://www.cnblogs.com/seyjs/p/12000533.html
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) == k:
            return 0
        if k == 1:
            return self.to_palindrome_min_change(s, 0, len(s) - 1)

        # dp[i][j] := min change needed to seperate s[:(i + 1)] into (j + 1) palindrome substrings
        dp = [[len(s)] * k for _ in s]
        dp[0][0] = 0
        for i in range(len(s)):
            for j in range(k):
                if j == 0:
                    dp[i][j] = self.to_palindrome_min_change(s, 0, i)
                else:
                    for m in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[m][j - 1] + self.to_palindrome_min_change(s, m + 1, i))

        return dp[-1][-1]

    def to_palindrome_min_change(self, string, start_index, end_index):
        if start_index == end_index:
            return 0

        min_change = 0
        left_middle_index  = (start_index + end_index) // 2
        right_middle_index = left_middle_index + 1 if (end_index - start_index) % 2 == 1 else left_middle_index
        radius = 0
        while left_middle_index - radius >= start_index and right_middle_index + radius <= end_index:
            if string[left_middle_index - radius] != string[right_middle_index + radius]:
                min_change += 1
            radius += 1

        return min_change

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(kn^2)
# Space Complexity: O(kn + n^2)
# -----------------------------------------
# Ref: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1278-palindrome-partitioning-iii/
import functools

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def to_palindrome_changes(start_index, end_index):
            if end_index <= start_index:
                return 0
            return to_palindrome_changes(start_index + 1, end_index - 1) + (1 if s[start_index] != s[end_index] else 0)

        if len(s) == k:
            return 0
        if k == 1:
            return to_palindrome_changes(0, len(s) - 1)

        # dp[i][j] := min change needed to seperate s[:(i + 1)] into (j + 1) palindrome substrings
        dp = [[len(s)] * k for _ in s]
        dp[0][0] = 0
        for i in range(len(s)):
            for j in range(k):
                if j == 0:
                    dp[i][j] = to_palindrome_changes(0, i)
                else:
                    for m in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[m][j - 1] + to_palindrome_changes(m + 1, i))

        return dp[-1][-1]
