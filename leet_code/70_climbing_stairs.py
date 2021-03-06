# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Note: space complexity of range in python3 is O(1) (ref: https://stackoverflow.com/a/46801951)
class Solution:
    def climbStairs(self, n):
        num_1 = 1
        num_2 = 1
        for _ in range(2, n + 1):
            num_1, num_2 = num_2, num_1 + num_2

        return num_2
