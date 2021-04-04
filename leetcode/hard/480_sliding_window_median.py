# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nk)
# Space Complexity: O(n + k)
# -----------------------------------------
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        curr_nums = sorted(nums[:k])

        medians = [self.median_of(curr_nums)]
        for index in range(k, len(nums)):
            curr_nums.pop(bisect.bisect_left(curr_nums, nums[index - k]))
            bisect.insort(curr_nums, nums[index])
            medians.append(self.median_of(curr_nums))

        return medians

    def median_of(self, nums: List[int]) -> float:
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]
