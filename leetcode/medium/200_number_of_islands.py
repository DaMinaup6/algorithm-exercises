# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(grid), n := len(grid[0])
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_mark_grid = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def fill_up(i, j, island_mark):
            if self.is_land(grid, i, j) and island_mark_grid[i][j] == -1:
                island_mark_grid[i][j] = island_mark
                fill_up(i - 1, j, island_mark)
                fill_up(i, j - 1, island_mark)
                fill_up(i + 1, j, island_mark)
                fill_up(i, j + 1, island_mark)

        current_island_mark = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.is_land(grid, i, j) and island_mark_grid[i][j] == -1:
                    current_island_mark += 1
                    fill_up(i, j, current_island_mark)

        return current_island_mark

    def is_land(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1'
