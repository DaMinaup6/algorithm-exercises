# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(n))
# Space Complexity: O(log(n))
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/79526571

'''
e.g. n == 8

                                    [1, 2, 3, 4, 5, 6, 7, 8]
Step 1 - remove from left to right: [   2,    4,    6,    8] == [num * 2 for num in range(1, n // 2 + 1)]
Step 2 - remove from right to left: [   2,          6      ] == [(num * 2 - 1) * 2 for num in range(1, (n // 2) // 2 + 1)]
Step 3 - remove from left to right: [               6      ] == [((num * 2) * 2 - 1) * 2 for num in range(1, ((n // 2) // 2) // 2 + 1)]

just like this
                                    [1, 2, 3, 4, 5, 6, 7, 8]
Step 1 - remove from left to right: [   1,    2,    3,    4] * 2
Step 2 - remove from right to left: [   1,          2      ] * 2 - 1
Step 3 - remove from left to right: [               1      ] * 2
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.leftToRight(n)

    def leftToRight(self, n):
        if n == 1:
            return 1

        return 2 * self.rightToLeft(n // 2)

    def rightToLeft(self, n):
        if n == 1:
            return 1

        if n % 2 == 0:
            return 2 * self.leftToRight(n // 2) - 1
        else:
            return 2 * self.leftToRight(n // 2)
