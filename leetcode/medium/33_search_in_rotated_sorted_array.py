class Solution:
    def search_in_sorted_array(self, nums, target):
        if len(nums) < 1 or target < nums[0] or target > nums[-1]:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        begin_index = 0
        end_index   = len(nums) - 1
        while begin_index < end_index:
            if target == nums[begin_index]:
                return begin_index
            if target == nums[end_index]:
                return end_index
            middle_index = (begin_index + end_index) // 2
            if target == nums[middle_index]:
                return middle_index

            if target > nums[middle_index]:
                begin_index = middle_index + 1
            else:
                end_index = middle_index - 1

        return -1

    def find_pivot(self, nums):
        if len(nums) <= 1 or nums[0] < nums[-1]: # nums[0] should be bigger than nums[-1] if there exists a pivot
            return -1
        elif len(nums) == 2:
            return 1

        begin_index = 0
        end_index   = len(nums) - 1
        while begin_index < end_index:
            middle_index = (begin_index + end_index) // 2
            if nums[middle_index - 1] > nums[middle_index]:
                return middle_index
            elif nums[middle_index] > nums[middle_index + 1]:
                return middle_index + 1

            if nums[middle_index] > nums[0]:
                begin_index = middle_index + 1
            else:
                end_index = middle_index - 1

        return -1

    def search(self, nums, target):
        if len(nums) < 1:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.find_pivot(nums)
        if pivot == -1:
            return self.search_in_sorted_array(nums, target)
        elif target >= nums[0]:
            return self.search_in_sorted_array(nums[:pivot], target)
        else:
            target_index = self.search_in_sorted_array(nums[pivot:], target)
            return target_index + pivot if target_index != -1 else -1

processor = Solution()
print(f"processor.search([   4, 5, 6, 7, 0, 1, 2], 3) == -1: {processor.search([4, 5, 6, 7, 0, 1, 2], 3) == -1}")
print(f"processor.search([   4, 5, 6, 7, 0, 1, 2], 0) ==  4: {processor.search([4, 5, 6, 7, 0, 1, 2], 0) == 4}")
print(f"processor.search([7, 8, 1, 2, 3, 4, 5, 6], 2) ==  3: {processor.search([7, 8, 1, 2, 3, 4, 5, 6], 2) == 3}")
