# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left  = 1
        right = x
        while left <= right:
            middle = (left + right) // 2
            middle_square = middle ** 2
            if middle_square == x:
                return middle
            elif middle_square > x:
                right = middle - 1
            else:
                left = middle + 1
        return left - 1

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = x
        while ans ** 2 > x:
            ans = (ans + x / ans) // 2

        return int(ans)
