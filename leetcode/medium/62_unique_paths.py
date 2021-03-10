# -----------------------------------------
# My Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

class Solution:
    def uniquePaths(self, m, n):
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))

# -----------------------------------------
# Faster Solution: Use math module
# -----------------------------------------
# import math
#
# class Solution:
#     def uniquePaths(self, m, n):
#         return math.comb(m + n - 2, m - 1)
