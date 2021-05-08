# -----------------------------------------
# My Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/happy-number/discuss/356519/Time-and-space-complexity-explanation
class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set([n])
        curr_num  = n

        while True:
            next_num = 0
            for char in str(curr_num):
                next_num += pow(int(char), 2)

            if next_num == 1:
                return True
            if next_num in seen_nums:
                return False

            curr_num = next_num
            seen_nums.add(curr_num)
