# -----------------------------------------
# Model Solution
#
# Time  Complexity: O((mn)^2)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(heightMap), n := len(heightMap[0])
# Ref: https://blog.csdn.net/XX_123_1_RJ/article/details/81089495
import collections

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        m, n = len(heightMap), len(heightMap[0])

        peaks_map = [[float('inf')] * n for _ in range(m)]
        start_positions = collections.deque()
        for row_idx in [0, m - 1]:
            for col_idx in range(n):
                peaks_map[row_idx][col_idx] = heightMap[row_idx][col_idx]
                start_positions.append((row_idx, col_idx))
        for row_idx in range(m):
            for col_idx in [0, n - 1]:
                peaks_map[row_idx][col_idx] = heightMap[row_idx][col_idx]
                start_positions.append((row_idx, col_idx))

        while len(start_positions) > 0:
            row_idx, col_idx = start_positions.popleft()
            for row_idx_move, col_idx_move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row_idx = row_idx + row_idx_move
                new_col_idx = col_idx + col_idx_move
                if new_row_idx <= 0 or new_row_idx >= m - 1 or new_col_idx <= 0 or new_col_idx >= n - 1:
                    continue

                peak_limit = max(peaks_map[row_idx][col_idx], heightMap[new_row_idx][new_col_idx])
                if peaks_map[new_row_idx][new_col_idx] > peak_limit:
                    peaks_map[new_row_idx][new_col_idx] = peak_limit
                    start_positions.append((new_row_idx, new_col_idx))

        return sum(peaks_map[row_idx][col_idx] - heightMap[row_idx][col_idx] for row_idx in range(1, m - 1) for col_idx in range(1, n - 1))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn * log(mn))
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(heightMap), n := len(heightMap[0])
# Ref: https://leetcode.com/problems/trapping-rain-water-ii/discuss/1102599/Python3-easy-and-readable
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        visited_map = [[False] * n for _ in range(m)]
        start_positions = []
        for row_idx in [0, m - 1]:
            for col_idx in range(n):
                heapq.heappush(start_positions, (heightMap[row_idx][col_idx], row_idx, col_idx))
                visited_map[row_idx][col_idx] = True
        for row_idx in range(m):
            for col_idx in [0, n - 1]:
                heapq.heappush(start_positions, (heightMap[row_idx][col_idx], row_idx, col_idx))
                visited_map[row_idx][col_idx] = True

        total_trapped_water = 0
        while len(start_positions) > 0:
            curr_height, row_idx, col_idx = heapq.heappop(start_positions)
            for row_idx_move, col_idx_move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_row_idx = row_idx + row_idx_move
                next_col_idx = col_idx + col_idx_move
                if next_row_idx <= 0 or next_row_idx >= m - 1 or next_col_idx <= 0 or next_col_idx >= n - 1 or visited_map[next_row_idx][next_col_idx]:
                    continue

                next_height = heightMap[next_row_idx][next_col_idx]
                if curr_height > next_height:
                    total_trapped_water += curr_height - next_height
                heapq.heappush(start_positions, (max(curr_height, next_height), next_row_idx, next_col_idx))
                visited_map[next_row_idx][next_col_idx] = True

        return total_trapped_water
