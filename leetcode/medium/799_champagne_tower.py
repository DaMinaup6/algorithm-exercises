# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(r^2)
# Space Complexity: O(r)
# -----------------------------------------
# r := query_row
# Ref: https://leetcode.com/problems/champagne-tower/solution/
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr_flow = [0] * (query_row + 1)
        curr_flow[0] = poured
        for row in range(query_row):
            next_flow = [0] * (query_row + 1)
            for col in range(row + 1):
                quantity_for_next_row = (curr_flow[col] - 1) / 2
                if quantity_for_next_row > 0:
                    next_flow[col]     += quantity_for_next_row
                    next_flow[col + 1] += quantity_for_next_row
            curr_flow = next_flow

        return min(curr_flow[query_glass], 1)
