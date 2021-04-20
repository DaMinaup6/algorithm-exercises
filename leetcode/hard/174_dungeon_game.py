# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(dungeon), n := len(dungeon[0])
# Ref:  https://blog.csdn.net/fuxuemingzhu/article/details/85341002
# TODO: Reduce space complexity if possible
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_len = len(dungeon)
        col_len = len(dungeon[0])
        # min_hp[i][j] := min hp required to move from bottom-right corner to min_hp[i][j] if started at (i, j)
        min_hp  = [[float('inf')] * (col_len + 1) for _ in range(row_len + 1)]
        min_hp[row_len][col_len - 1] = min_hp[row_len - 1][col_len] = 1

        for row_idx in range(row_len - 1, -1, -1):
            for col_idx in range(col_len - 1, -1, -1):
                min_hp[row_idx][col_idx] = max(1, min(min_hp[row_idx + 1][col_idx], min_hp[row_idx][col_idx + 1]) - dungeon[row_idx][col_idx])
        return min_hp[0][0]
