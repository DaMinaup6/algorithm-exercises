# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        abs_diff = []
        diff_sum = 0
        all_zero = True
        for index in range(len(nums1)):
            diff = abs(nums1[index] - nums2[index])
            if diff > 0:
                all_zero = False
            diff_sum += diff
            heapq.heappush(abs_diff, (-diff, index))
        if all_zero:
            return 0

        nums1_set  = set(nums1)
        max_reduce = 0
        while len(abs_diff) > 0:
            diff, num2_index = heapq.heappop(abs_diff)
            diff *= -1
            if max_reduce >= diff:
                break
            
            min_diff = diff
            for num1 in nums1_set:
                min_diff = min(min_diff, abs(num1 - nums2[num2_index]))
            max_reduce = max(max_reduce, diff - min_diff)

        return (diff_sum - max_reduce) % MOD

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://leetcode.com/problems/minimum-absolute-sum-difference/discuss/1141447/Python-Binary-Search
# b) http://uranusjr.logdown.com/posts/2013/08/11/python-zip-so-did-unzip
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7

        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))
        abs_diff_arr = [abs(nums1[index] - nums2[index]) for index in range(len(nums1))]
        max_decrease = 0
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                j = bisect.bisect_left(nums1, nums2[i])
                if j == len(nums1):
                    max_decrease = max(max_decrease, abs_diff_arr[i] - abs(nums1[-1] - nums2[i]))
                elif j == 0:
                    max_decrease = max(max_decrease, abs_diff_arr[i] - abs(nums1[0] - nums2[i]))
                else:
                    new_diff = min(abs(nums1[j] - nums2[i]), abs(nums1[j - 1] - nums2[i]))
                    max_decrease = max(max_decrease, abs_diff_arr[i] - new_diff)

        return (sum(abs_diff_arr) - max_decrease) % MOD
