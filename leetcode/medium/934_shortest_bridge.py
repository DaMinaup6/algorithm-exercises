# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mn)
# Space Complexity: O(mn)
# -----------------------------------------
# m := len(A), n := len(A[0])
# Ref: https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf

from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        island_positions = deque()
        def dfs(i, j):
            if not (0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 1):
                return
            
            A[i][j] = 2
            island_positions.append((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs_done = False
        for i in range(len(A)):
            if dfs_done:
                break
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    continue
                if A[i][j] == 1:
                    dfs(i, j)
                    dfs_done = True
                    break

        distance = 0
        while len(island_positions) > 0:
            positions_size = len(island_positions)
            for _ in range(positions_size):
                position = island_positions.popleft()

                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_position = (position[0] + direction[0], position[1] + direction[1])
                    if 0 <= new_position[0] < len(A) and 0 <= new_position[1] < len(A[0]):
                        if A[new_position[0]][new_position[1]] == 1:
                            return distance
                        elif A[new_position[0]][new_position[1]] == 0:
                            island_positions.append(new_position)
                            A[new_position[0]][new_position[1]] = 2
            distance += 1

        return -1
