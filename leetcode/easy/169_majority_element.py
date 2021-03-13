# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
            if num_count[num] > len(nums) // 2:
                return num

# -----------------------------------------
# Boyer-Moore Voting Algorithm
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate
