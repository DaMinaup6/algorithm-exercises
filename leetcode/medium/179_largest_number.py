# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/largest-number/solution/

# -----> Version 1
class NumberComparator(str):
    def __lt__(x, y):
        return y + x < x + y

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        combined_num_str = ''.join(sorted(map(str, nums), key=NumberComparator))
        return combined_num_str if combined_num_str[0] != '0' else '0'

# -----> Version 2
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def num_comparator(x, y):
            return int(y + x) - int(x + y)

        combined_num_str = ''.join(sorted(map(str, nums), key=cmp_to_key(num_comparator)))
        return combined_num_str if combined_num_str[0] != '0' else '0'
