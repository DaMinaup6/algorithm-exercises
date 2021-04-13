# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(triangle)
from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_cumulative_sums = [triangle[0][0]]
        curr_cumulative_sums = [0, 0]
        for layer in range(1, len(triangle)):
            for index in range(len(triangle[layer])):
                if index == 0:
                    curr_cumulative_sums[0] = triangle[layer][0] + prev_cumulative_sums[0]
                elif index == layer:
                    curr_cumulative_sums[-1] = triangle[layer][-1] + prev_cumulative_sums[-1]
                else:
                    curr_cumulative_sums[index] = triangle[layer][index] + min(prev_cumulative_sums[index], prev_cumulative_sums[index - 1])

            prev_cumulative_sums = curr_cumulative_sums
            curr_cumulative_sums = [0] * (layer + 2)
        
        return min(prev_cumulative_sums)
