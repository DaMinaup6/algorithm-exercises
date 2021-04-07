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

# -----------------------------------------
# Backtracking
#
# Time  Complexity: O(2^n)
# Space Complexity: O(2^n)
# -----------------------------------------
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(subset_size, start_index, curr_subset):
            if len(curr_subset) == subset_size:
                output.append(curr_subset.copy())
                return

            for index in range(start_index, len(nums)):
                curr_subset.append(nums[index])
                backtrack(subset_size, index + 1, curr_subset)
                curr_subset.pop()

        for subset_size in range(len(nums) + 1):
            backtrack(subset_size, 0, [])
        return output
