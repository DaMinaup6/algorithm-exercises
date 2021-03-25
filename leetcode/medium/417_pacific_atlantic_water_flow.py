# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(matrix), n := len(matrix[0])
# Ref: https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        # Initialize variables, including sets used to keep track of visited cells
        pacific_reachable  = set()
        atlantic_reachable = set()
        def dfs(row, col, reachable):
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                dfs(new_row, new_col, reachable)

        # Loop through each cell adjacent to the oceans and start a DFS
        for index in range(len(matrix)):
            dfs(index,                  0,  pacific_reachable)
            dfs(index, len(matrix[0]) - 1, atlantic_reachable)
        for index in range(len(matrix[0])):
            dfs(              0, index,  pacific_reachable)
            dfs(len(matrix) - 1, index, atlantic_reachable)
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
