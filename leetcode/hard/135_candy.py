# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1] and candies[index] <= candies[index - 1]:
                candies[index] = candies[index - 1] + 1
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1] and candies[index] <= candies[index + 1]:
                candies[index] = candies[index + 1] + 1

        return sum(candies)
