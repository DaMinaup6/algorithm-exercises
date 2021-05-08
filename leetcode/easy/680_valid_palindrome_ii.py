# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n^2)
# -----------------------------------------
from functools import lru_cache

class Solution:
    def validPalindrome(self, s: str) -> bool:
        @lru_cache(None)
        def dfs(left_pointer, right_pointer, char_deleted):
            if left_pointer >= right_pointer:
                return True
            if s[left_pointer] != s[right_pointer]:
                if char_deleted:
                    return False
                if s[left_pointer + 1] == s[right_pointer] and dfs(left_pointer + 1, right_pointer, True):
                    return True
                if s[left_pointer] == s[right_pointer - 1] and dfs(left_pointer, right_pointer - 1, True):
                    return True
                return False
            return dfs(left_pointer + 1, right_pointer - 1, char_deleted)

        return dfs(0, len(s) - 1, False)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/danspace1/article/details/88955337
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                left_removed_sub_string  = s[(left_pointer + 1):(right_pointer + 1)]
                right_removed_sub_string = s[left_pointer:right_pointer]
                return left_removed_sub_string == left_removed_sub_string[::-1] or right_removed_sub_string == right_removed_sub_string[::-1]
            left_pointer  += 1
            right_pointer -= 1

        return True
