# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=__yxFFRQAl8
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        curr_keep, curr_swap = 0, 1
        for index in range(1, len(nums1)):
            next_keep, next_swap = float('inf'), float('inf')
            if nums1[index] > nums1[index - 1] and nums2[index] > nums2[index - 1]:
                next_keep = curr_keep
                next_swap = curr_swap + 1
            if nums1[index] > nums2[index - 1] and nums2[index] > nums1[index - 1]:
                next_keep = min(next_keep, curr_swap)
                next_swap = min(next_swap, curr_keep + 1)
            curr_keep, curr_swap = next_keep, next_swap

        return min(curr_keep, curr_swap)
