# -----------------------------------------
# My Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(nums1), n := len(nums2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_element_index = {}
        for index, num in enumerate(nums2):
            nums2_element_index[num] = index

        nums2_next_greater_index = [-1] * len(nums2)
        stack = []
        for element_index in range(len(nums2) - 1, -1, -1):
            num = nums2[element_index]
            while len(stack) > 0 and nums2[stack[-1]] <= num:
                stack.pop()
            if len(stack) > 0:
                nums2_next_greater_index[element_index] = stack[-1]
            stack.append(element_index)

        output = []
        for num in nums1:
            next_greater_index = nums2_next_greater_index[nums2_element_index[num]]
            output.append(nums2[next_greater_index] if next_greater_index != -1 else -1)
        return output
