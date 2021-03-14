# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(n^3)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_score = 0
        for left_cursor in range(k + 1):
            for right_cursor in range(k, len(nums)):
                max_score = max(max_score, self.calc_score(nums, left_cursor, right_cursor))

        return max_score

    def calc_score(self, nums, i, j):
        return min(nums[i:(j + 1)]) * (j - i + 1)

# -----------------------------------------
# Model Solution: Greedy
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        min_num, max_score = nums[k], nums[k]

        left_cursor, right_cursor = k, k
        while left_cursor != 0 or right_cursor != len(nums) - 1:
            if left_cursor == 0 or (right_cursor < len(nums) - 1 and nums[left_cursor - 1] <= nums[right_cursor + 1]):
                right_cursor += 1
                min_num = min(min_num, nums[right_cursor])
            else:
                left_cursor -= 1
                min_num = min(min_num, nums[left_cursor])
            max_score = max(max_score, min_num * (right_cursor - left_cursor + 1))

        return max_score
