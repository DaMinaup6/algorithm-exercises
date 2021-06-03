# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(log(m + n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://coderscat.com/leetcode-median-of-two-sorted-arrays/
def find_kth(k, nums1, nums2):
    if len(nums1) == 0:
        return nums2[k]
    if len(nums2) == 0:
        return nums1[k]

    mid_idx_1 = len(nums1) // 2
    mid_idx_2 = len(nums2) // 2
    # left_part                                      |  right_part
    # nums1[0], nums1[1], ..., nums1[mid_idx_1 - 1]  |  nums1[mid_idx_1], nums1[mid_idx_1 + 1], ..., nums1[m - 1]
    # nums2[0], nums2[1], ..., nums2[mid_idx_2 - 1]  |  nums2[mid_idx_2], nums2[mid_idx_2 + 1], ..., nums2[n - 1]
    if k > mid_idx_1 + mid_idx_2:
        # e.g. nums1 == [1], nums2 == [2] and k == 1
        #      if use something like find_kth(k - mid_idx_1, nums1[mid_idx_1:], nums2)
        #      then the loop never ends
        if nums1[mid_idx_1] > nums2[mid_idx_2]:
            return find_kth(k - (mid_idx_2 + 1), nums1, nums2[(mid_idx_2 + 1):])
        else:
            return find_kth(k - (mid_idx_1 + 1), nums1[(mid_idx_1 + 1):], nums2)
    else:
        # cannot return find_kth(k, nums1[:mid_idx_1], nums2[:mid_idx_2]) directly here
        # e.g. nums1 == [1, 2, 3], nums2 == [100, 101, 102, 103, 104, 105, 106] and k == 3
        #      the answer would be 3, but if we return find_kth(k, nums1[:mid_idx_1], nums2[:mid_idx_2]) then we get wrong answer
        if nums1[mid_idx_1] > nums2[mid_idx_2]:
            return find_kth(k, nums1[:mid_idx_1], nums2)
        else:
            return find_kth(k, nums1, nums2[:mid_idx_2])

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            middle_left_index  = total_len // 2 - 1
            middle_right_index = total_len // 2
            return (find_kth(middle_left_index, nums1, nums2) + find_kth(middle_right_index, nums1, nums2)) / 2
        return find_kth(total_len // 2, nums1, nums2)
