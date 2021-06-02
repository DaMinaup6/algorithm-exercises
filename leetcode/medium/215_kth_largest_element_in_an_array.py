# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# -----------------------------------------
# Model Solution: Quick Select 1
#
# Time  Complexity: average - O(n), worst - O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        nums1, nums2 = [], []
        for num in nums:
            if num < pivot:
                nums1.append(num)
            elif num > pivot:
                nums2.append(num)

        if k <= len(nums2):
            return self.findKthLargest(nums2, k)
        elif k > len(nums) - len(nums1):
            return self.findKthLargest(nums1, k - (len(nums) - len(nums1)))

        return pivot

# -----------------------------------------
# Model Solution: Quick Select 2
#
# Time  Complexity: average - O(n), worst - O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = self.partition(nums, left, right)
            if pivot_idx == len(nums) - k:
                return nums[pivot_idx]
            elif pivot_idx > len(nums) - k:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

    def partition(self, nums, start_index, end_index):
        pivot = nums[end_index]

        pivot_index = start_index - 1
        for num_index in range(start_index, end_index):
            if nums[num_index] <= pivot:
                pivot_index += 1
                nums[pivot_index], nums[num_index] = nums[num_index], nums[pivot_index]

        pivot_index += 1
        nums[pivot_index], nums[end_index] = nums[end_index], nums[pivot_index]
        return pivot_index
