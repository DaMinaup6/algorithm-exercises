# -----------------------------------------
# Model Solution
#
# Time Complexity: O(mn)
# -----------------------------------------
# m := len(dungeon), n := len(dungeon[0])
# Ref:  https://blog.csdn.net/fuxuemingzhu/article/details/85341002

# -----> Version 1: Space Complexity: O(mn)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_len, col_len = len(dungeon), len(dungeon[0])
        # min_hp[i][j] := min hp required to move from bottom-right corner to min_hp[i][j] if started at (i, j)
        min_hp = [[float('inf')] * (col_len + 1) for _ in range(row_len + 1)]
        min_hp[row_len][col_len - 1] = min_hp[row_len - 1][col_len] = 1

        for row_idx in range(row_len - 1, -1, -1):
            for col_idx in range(col_len - 1, -1, -1):
                # for each ceill we need at least 1 hp so need a max(1, ...) here
                min_hp[row_idx][col_idx] = max(1, min(min_hp[row_idx + 1][col_idx], min_hp[row_idx][col_idx + 1]) - dungeon[row_idx][col_idx])
        return min_hp[0][0]

# -----> Version : Space Complexity: O(n)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_len, col_len = len(dungeon), len(dungeon[0])

        next_min_hp = [float('inf')] * (col_len + 1)
        curr_min_hp = [float('inf')] * (col_len + 1)
        curr_min_hp[col_len - 1] = next_min_hp[col_len] = 1

        for row_idx in range(row_len - 1, -1, -1):
            for col_idx in range(col_len - 1, -1, -1):
                next_min_hp[col_idx] = max(1, min(curr_min_hp[col_idx], next_min_hp[col_idx + 1]) - dungeon[row_idx][col_idx])
            curr_min_hp, next_min_hp = next_min_hp, [float('inf')] * (col_len + 1)
        return curr_min_hp[0]
