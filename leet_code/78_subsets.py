# -----------------------------------------
# My Solution (Recursive)
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
class Solution:
    def subsets(self, nums):
        subsets = [[]]

        def generate_subset(current_subset, start_index, subset_size):
            for i in range(start_index, len(nums)):
                if subset_size == 1:
                    subsets.append(current_subset + [nums[i]])
                else:
                    generate_subset(current_subset + [nums[i]], i + 1, subset_size - 1)

        for size in range(1, len(nums) + 1):
            generate_subset([], 0, size)

        return subsets
