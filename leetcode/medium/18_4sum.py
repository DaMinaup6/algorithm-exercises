# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n^4)
# -----------------------------------------
import itertools

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        all_four_nums = set()
        for index_1, index_2 in itertools.combinations(range(len(nums)), 2):
            for num_1, num_2 in self.all_two_sums(nums, target - nums[index_1] - nums[index_2], set([index_1, index_2])):
                four_num = sorted([nums[index_1], nums[index_2], num_1, num_2])
                all_four_nums.add(tuple(four_num))
        return all_four_nums

    def all_two_sums(self, nums: List[int], target: int, skip_indexes: set[int]) -> List[int]:
        num_count = {}
        for index, num in enumerate(nums):
            if index in skip_indexes:
                continue
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        all_two_sums = set()
        for index, num in enumerate(nums):
            if index in skip_indexes:
                continue
            if target - num == num:
                if num_count[num] >= 2:
                    all_two_sums.add((num, num))
            elif target - num in num_count:
                all_two_sums.add((num, target - num))
        return all_two_sums

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n^4)
# -----------------------------------------
# Ref: https://leetcode.com/problems/4sum/discuss/292934/python-hashmap-64ms
import collections

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4 or 4 * nums[0] > target or 4 * nums[-1] < target:
            return []
        # use defaultdic for better performance
        diff_indexes_dict = collections.defaultdict(list)
        results = set()

        for index_1 in range(len(nums) - 1):
            for index_2 in range(index_1 + 1, len(nums)):
                diff = target - nums[index_1] - nums[index_2]
                diff_indexes_dict[diff].append((index_1, index_2))

        for index_1 in range(len(nums) - 3):
            for index_2 in range(index_1 + 1, len(nums)):
                total = nums[index_1] + nums[index_2]
                if total in diff_indexes_dict:
                    for indexes in diff_indexes_dict[total]:
                        # Exclude the case indexes[0] or indexes[1] is index_1 or index_2
                        if indexes[0] > index_2:
                            results.add((nums[index_1], nums[index_2], nums[indexes[0]], nums[indexes[1]]))
        return results
