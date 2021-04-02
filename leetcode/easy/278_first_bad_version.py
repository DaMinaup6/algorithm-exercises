# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# -----------------------------------------
# My Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def firstBadVersion(self, n):
        left  = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left
