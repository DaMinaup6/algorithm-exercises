def find_kth(k, nums1, nums2):
    if len(nums1) == 0:
        return nums2[k]
    if len(nums2) == 0:
        return nums1[k]

    mid_idx_1 = len(nums1) // 2
    mid_idx_2 = len(nums2) // 2

    if k > mid_idx_1 + mid_idx_2:
        if nums1[mid_idx_1] > nums2[mid_idx_2]:
            return find_kth(k - mid_idx_2 - 1, nums1, nums2[(mid_idx_2 + 1):])
        else:
            return find_kth(k - mid_idx_1 - 1, nums1[(mid_idx_1 + 1):], nums2)
    else:
        if nums1[mid_idx_1] > nums2[mid_idx_2]:
            return find_kth(k, nums1[:mid_idx_1], nums2)
        else:
            return find_kth(k, nums1, nums2[:mid_idx_2])

def findMedianSortedArrays(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 0:
        return (find_kth(total_len // 2 - 1, nums1, nums2) + find_kth(total_len // 2, nums1, nums2)) / 2

    return find_kth(total_len // 2, nums1, nums2)
