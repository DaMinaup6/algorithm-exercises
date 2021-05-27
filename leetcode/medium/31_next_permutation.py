# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/next-permutation/solution/
# b) https://www.youtube.com/watch?v=quAS1iydq7U
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find out the longest decreasing sub-array since it's on the last permutation
        # e.g. nums == [6, 2, 1, 5, 4, 3, 0]
        #                     ^
        # notice that [5, 4, 3, 0] is decreasing sub-array, for this sub-array it's already on its last permutation (largest permutation)
        # that's what i here means
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # again, use nums == [6, 2, 1, 5, 4, 3, 0] as example
        # we find that i points to the number 1, so for next permutation, we need to find a number greater than 1
        # the number must exists since sub-array before it is decreasing
        # so we will find j points to number 3
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # after swap nums[i] and nums[j], we get nums == [6, 2, 3, 5, 4, 1, 0]
        # since [5, 4, 3, 0] is decreasing sub-array, so [5, 4, 1, 0] must be decreasing sub-array (since nums[i] < nums[j])
        # so [5, 4, 1, 0] is on its last permutation because [5, 4, 1, 0] is decreasing sub-array
        # then we need to reverse it to make it the first permutation (smallest permutation)
        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
