# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(Cat(n))
# Space Complexity: O(n * Cat(n))
# -----------------------------------------
# Cat(n) is Catalan number, Cat(n) := math.comb(2n, n) / (n + 1)
# Ref:
# a) https://www.youtube.com/watch?v=gxYV8eZY0eQ
# b) https://massivealgorithms.blogspot.com/2015/07/leetcodedifferent-ways-to-add.html
# c) https://blog.csdn.net/qq_30115697/article/details/88906534
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def possible_nums(string):
            nums = []
            for index, char in enumerate(string):
                if char in '+-*':
                    left_nums  = possible_nums(string[:index])
                    right_nums = possible_nums(string[(index + 1):])

                    for left_num in left_nums:
                        for right_num in right_nums:
                            if char == '+':
                                nums.append(left_num + right_num)
                            elif char == '-':
                                nums.append(left_num - right_num)
                            else:
                                nums.append(left_num * right_num)
            return nums if len(nums) > 0 else [int(string)]

        return possible_nums(expression)
