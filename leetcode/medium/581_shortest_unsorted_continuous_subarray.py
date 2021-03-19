# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_num = nums[0]

        sort_range = None
        for index in range(1, len(nums)):
            if nums[index] < nums[0]:
                sort_range = [0, index]
            elif nums[index] < max_num:
                cursor = 1
                while cursor < index and nums[cursor] <= nums[index]:
                    cursor += 1

                if sort_range is None:
                    sort_range = [cursor, index]
                else:
                    sort_range = [min(sort_range[0], cursor), index]
            elif nums[index] > max_num:
                max_num = nums[index]

        return sort_range[1] - sort_range[0] + 1 if sort_range is not None else 0

# -----------------------------------------
# Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=BS30yX9WwI8
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        cursor_l = 0
        cursor_r = len(nums) - 1

        while cursor_l < cursor_r and nums[cursor_l] <= nums[cursor_l + 1]:
            cursor_l += 1
        if cursor_l == cursor_r:
            return 0
        while cursor_r > cursor_l and nums[cursor_r] >= nums[cursor_r - 1]:
            cursor_r -= 1

        range_min, range_max = float('inf'), -float('inf')
        for index in range(cursor_l, cursor_r + 1):
            range_min = min(range_min, nums[index])
            range_max = max(range_max, nums[index])

        while cursor_l > 0 and nums[cursor_l - 1] > range_min:
            cursor_l -= 1
        while cursor_r < len(nums) - 1 and nums[cursor_r + 1] < range_max:
            cursor_r += 1

        return cursor_r - cursor_l + 1
