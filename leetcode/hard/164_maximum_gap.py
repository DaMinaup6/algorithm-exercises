# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref:
# a) https://www.jianshu.com/p/dbb8056344ea
# b) https://www.youtube.com/watch?v=qN0qvtFbCYw
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        min_num, max_num = min(nums), max(nums)
        if max_num == min_num:
            return 0

        # after ignoring min_num and max_num, there are still len(nums) - 2 numbers left, so we need len(nums) - 1 buckets to make sure there would be a empty bucket after
        # assigning all numbers to buckets
        bucket_size = math.ceil((max_num - min_num) / (len(nums) - 1))
        # if max_num - min_num is multiplier of len(nums) - 1, then when num == max_num, bucket index would be len(nums) - 1 so still we need len(nums) buckets here
        buckets = [[float('inf'), -float('inf')] for _ in range(len(nums))]
        for num in nums:
            bucket = buckets[(num - min_num) // bucket_size]
            bucket[0] = min(bucket[0], num)
            bucket[1] = max(bucket[1], num)
        buckets = [bucket for bucket in buckets if bucket[0] != float('inf')]

        return max(buckets[index][0] - buckets[index - 1][1] for index in range(1, len(buckets)))
