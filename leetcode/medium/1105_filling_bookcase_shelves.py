# -----------------------------------------
# Model Solution: Dynamic Programming
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/Orientliu96/article/details/104071164
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range (1, n + 1):
            max_width  = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[-1]
