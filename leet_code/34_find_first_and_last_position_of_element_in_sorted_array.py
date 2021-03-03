# -----------------------------------------
# Original
# -----------------------------------------
class Solution:
    def find_first_target(self, nums, target):
        if nums[0] == target:
            return 0

        left_cursor  = 0
        right_cursor = len(nums) - 1
        while left_cursor <= right_cursor:
            if nums[left_cursor] == target and nums[left_cursor - 1] != target:
                return left_cursor

            if nums[left_cursor] == target:
                right_cursor = left_cursor - 1
                left_cursor  = 0
            else:
                middle_index = (left_cursor + right_cursor) // 2
                if target == nums[middle_index]:
                    left_cursor = middle_index
                elif target > nums[middle_index]:
                    left_cursor = middle_index + 1
                else:
                    right_cursor = middle_index - 1

        return -1

    def find_last_target(self, nums, target):
        if nums[-1] == target:
            return len(nums) - 1

        left_cursor  = 0
        right_cursor = len(nums) - 1
        while left_cursor <= right_cursor:
            if nums[right_cursor] == target and nums[right_cursor + 1] != target:
                return right_cursor

            if nums[right_cursor] == target:
                left_cursor  = right_cursor + 1
                right_cursor = len(nums) - 1
            else:
                middle_index = (left_cursor + right_cursor) // 2
                if target == nums[middle_index]:
                    right_cursor = middle_index
                elif target < nums[middle_index]:
                    right_cursor = middle_index - 1
                else:
                    left_cursor = middle_index + 1

        return -1

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        return [self.find_first_target(nums, target), self.find_last_target(nums, target)]

processor = Solution()
print(f"processor.searchRange([5, 7, 7, 8, 8, 10], 8) == [ 3,  4]: {processor.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]}")
print(f"processor.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]: {processor.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]}")
