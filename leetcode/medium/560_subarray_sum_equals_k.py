# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        for window_size in range(1, len(nums) + 1):
            current_sum = sum(nums[0:window_size])
            if current_sum == k:
                result += 1

            for index in range(1, len(nums) - window_size + 1):
                current_sum -= nums[index - 1]
                current_sum += nums[index + window_size - 1]
                if current_sum == k:
                    result += 1

        return result

# -----------------------------------------
# Cumulative Sum
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/subarray-sum-equals-k/solution/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0] * (len(nums) + 1)
        for index in range(1, len(nums) + 1):
            sums[index] = sums[index - 1] + nums[index - 1]

        result = 0
        for start_index in range(len(nums)):
            for end_index in range(start_index + 1, len(nums) + 1):
                if sums[end_index] - sums[start_index] == k:
                    result += 1

        return result

# -----------------------------------------
# Hashmap
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/subarray-sum-equals-k/solution/

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1

        current_sum, result = 0, 0
        for index in range(len(nums)):
            current_sum += nums[index]
            if current_sum - k in count_map:
                result += count_map[current_sum - k]
            count_map[current_sum] += 1

        return result
