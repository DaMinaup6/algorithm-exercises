# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(nums1), n := len(nums1)
# Ref:  https://leetcode.com/problems/intersection-of-two-arrays/solution/245850
# NOTE: suppose nums1 and nums2 are sorted, find a solution with time complexity O(m + n) and space complexity O(1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return []
        # for real interview question, nums1 and nums2 are supposed to be sorted
        nums1.sort()
        nums2.sort()

        intersection = []
        nums1_cursor = 0
        nums2_cursor = 0
        while nums1_cursor < len(nums1) and nums2_cursor < len(nums2):
            num1 = nums1[nums1_cursor]
            num2 = nums2[nums2_cursor]
            if num1 == num2:
                intersection.append(num1)
                while nums1_cursor < len(nums1) and nums1[nums1_cursor] == num1:
                    nums1_cursor += 1
                while nums2_cursor < len(nums2) and nums2[nums2_cursor] == num2:
                    nums2_cursor += 1
            elif num1 < num2:
                while nums1_cursor < len(nums1) and nums1[nums1_cursor] == num1:
                    nums1_cursor += 1
            else:
                while nums2_cursor < len(nums2) and nums2[nums2_cursor] == num2:
                    nums2_cursor += 1

        return intersection
