# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n + max(nums))
# -----------------------------------------
# n := len(nums)
# Ref:
# a) https://leetcode.com/problems/sum-of-floored-pairs/discuss/1210858/Python-8-lines-frequency-prefix-sum
# b) https://www.youtube.com/watch?v=OM6oph-bDhE
# c) https://stackoverflow.com/questions/35326140/what-is-the-time-complexity-of-my-function
import collections

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        max_num = max(nums)
        num_counter = collections.Counter(nums)
        num_count_pre_sums = [0] * (max_num + 1)
        for num in range(1, max_num + 1):
            num_count_pre_sums[num] = num_count_pre_sums[num - 1] + num_counter[num]

        '''
        for a element x consider all pairs such that x is the denominator
        all numbers less than x will result in 0 (float division)
        now for elements greater than x, 
            numbers from     x to 2 * x - 1 will result in 1
            numbers from 2 * x to 3 * x - 1 will result in 2 and so on   

        so each number from     x to 2 * x - 1 will add 1 to the answer
           each number from 2 * x to 3 * x - 1 will add 2 to the answer 
           each number from 3 * x to 4 * x - 1 will add 3 to the answer and so on
        '''
        ans = 0
        for num in set(nums):
            for curr_num in range(num, max_num + 1, num):
                ans = (ans + num_counter[num] * (num_count_pre_sums[max_num] - num_count_pre_sums[curr_num - 1])) % MOD
        return ans
