# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
import collections

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_indexes_dict = collections.defaultdict(list)
        remainder_indexes_dict[nums[0] % k].append(0)
        cumulative_sum_remainders = [0] * len(nums)
        cumulative_sum_remainders[0] = nums[0] % k
        for index in range(1, len(nums)):
            remainder = (nums[index] + cumulative_sum_remainders[index - 1]) % k
            remainder_indexes_dict[remainder].append(index)
            cumulative_sum_remainders[index] = remainder
            if remainder == 0:
                return True
        if len(nums) <= 2:
            return False

        # e.g. nums == [23, 2, 4, 6, 8], k == 6
        # => cumulative_sums == [23, 25, 29, 35, 43]
        # => cumulative_sum_remainders == [5, 1, 5, 5, 1]
        # we can see that for index 3, if there exists same remainder 5 in index 1 or previous indexes (since min length of subarray is 2), then the sum of subarray is multiple of k
        # like in this case, remainder at index 0 is 5 so for subarray nums[(0 + 1):(3 + 1)] its sum is multiple of k
        prev_remainders = set([cumulative_sum_remainders[0], cumulative_sum_remainders[1]])
        for index in range(2, len(nums)):
            curr_remainder = cumulative_sum_remainders[index]
            # just need to check the very first index of curr_remainder to see if we can find a subarray with min length 2
            # e.g. nums == [1, 4, 0], k == 6
            # => cumulative_sum_remainders == [1, 5, 5]
            # at index 2 we see the remainder is 5 but the previous remainder 5 is at index 1, which means we cannot form a subarray with length >= 2 and its sum is multiple of k
            if curr_remainder in prev_remainders and index - remainder_indexes_dict[curr_remainder][0] > 1:
                return True
            prev_remainders.add(curr_remainder)
        return False

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(min(k, n))
# -----------------------------------------
# Ref: https://leetcode.com/problems/continuous-subarray-sum/discuss/236976/Python-solution
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_first_index_dict = {0: -1} # if we got cumulative_sum_mod == 0 at index 1, we should return True immediately so we need {0: -1} as init value
        cumulative_sum_mod = 0
        for index, num in enumerate(nums):
            cumulative_sum_mod = (cumulative_sum_mod + num) % k
            if cumulative_sum_mod not in remainder_first_index_dict:
                remainder_first_index_dict[cumulative_sum_mod] = index
            elif index - remainder_first_index_dict[cumulative_sum_mod] > 1:
                return True

        return False
