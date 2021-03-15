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
            pivot_idx = left
            new_pivot_idx = self.partition_around_pivot(left, right, pivot_idx, nums)

            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

    def partition_around_pivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right + 1):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx
