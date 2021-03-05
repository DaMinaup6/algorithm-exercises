# -----------------------------------------
# O(N^2): Brute Force
# -----------------------------------------
# class Solution:
#     def maxSubArray(self, nums):
#         max_sum = nums[0]
#         tmp_sum = nums[0]
#
#         for i in range(len(nums)):
#             tmp_sum = nums[i]
#             max_sum = max(max_sum, tmp_sum)
#             for j in range(i + 1, len(nums)):
#                 tmp_sum += nums[j]
#                 max_sum = max(max_sum, tmp_sum)
#
#         return max_sum

# -----------------------------------------
# O(Nlog(N)): Divide and Conquer
# -----------------------------------------
# def maxCrossingSum(arr, l, m, h):
#     # Include elements on left of mid.
#     sm = 0
#     left_sum = -10000
#
#     for i in range(m, l-1, -1):
#         sm = sm + arr[i]
#
#         if (sm > left_sum):
#             left_sum = sm
#
#     # Include elements on right of mid
#     sm = 0
#     right_sum = -1000
#     for i in range(m + 1, h + 1):
#         sm = sm + arr[i]
#
#         if (sm > right_sum):
#             right_sum = sm
#
#     # Return sum of elements on left and right of mid
#     # returning only left_sum + right_sum will fail for [-2, 1]
#     return max(left_sum + right_sum, left_sum, right_sum)
#
# # Returns sum of maxium sum subarray in aa[l..h]
# def maxSubArraySum(arr, l, h):
#     # Base Case: Only one element
#     if (l == h):
#         return arr[l]
#
#     # Find middle point
#     m = (l + h) // 2
#
#     # Return maximum of following three possible cases
#     # a) Maximum subarray sum in left half
#     # b) Maximum subarray sum in right half
#     # c) Maximum subarray sum such that the
#     #     subarray crosses the midpoint
#     return max(maxSubArraySum(arr, l, m), maxSubArraySum(arr, m+1, h), maxCrossingSum(arr, l, m, h))
#
# class Solution:
#     def maxSubArray(self, nums):
#         return maxSubArraySum(nums, 0, len(nums) - 1)

# -----------------------------------------
# O(N): Kadane's Algorithm
# -----------------------------------------
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        tmp_sum = nums[0]

        for num_idx in range(1, len(nums)):
            num = nums[num_idx]
            if tmp_sum < 0:
                tmp_sum = num
            else:
                tmp_sum += num
            max_sum = max(max_sum, tmp_sum)

        return max_sum
