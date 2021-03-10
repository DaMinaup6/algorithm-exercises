# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def beautySum(self, s):
        if len(s) <= 2:
            return 0

        beauty_sum = 0
        for i in range(len(s)):
            char_count_arr = [0 for _ in range(26)]
            char_count_arr[ord(s[i]) - 97] += 1

            for j in range(i + 1, len(s)):
                char_count_arr[ord(s[j]) - 97] += 1
                beauty_sum += (max(char_count_arr) - min(num for num in char_count_arr if num > 0))

        return beauty_sum
