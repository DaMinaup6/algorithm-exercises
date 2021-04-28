# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(k)
# -----------------------------------------
# n := len(nums)
# Ref: https://blog.csdn.net/qq_20141867/article/details/82024222
from collections import OrderedDict

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) <= 1 or k < 1 or t < 0:
            return False

        moving_window_set = OrderedDict()
        for num in nums:
            key = num // t if t != 0 else num
            for target_key in (key - 1, key, key + 1):
                if target_key in moving_window_set and abs(moving_window_set[target_key] - num) <= t:
                    return True

            if len(moving_window_set) == k:
                moving_window_set.popitem(False) # popitem(last=False)
            moving_window_set[key] = num

        return False

processor = Solution()
print(f"processor.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)       == True:  {processor.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)       == True}")
print(f"processor.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)       == True:  {processor.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)       == True}")
print(f"processor.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) == False: {processor.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) == False}")
