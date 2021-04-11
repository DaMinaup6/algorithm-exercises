# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
from collections import defaultdict, deque

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        lane_obstacles = defaultdict(deque)
        for index, obstacle_position in enumerate(obstacles):
            if obstacle_position != 0:
                lane_obstacles[obstacle_position].append(index)
        for lane in [1, 2, 3]:
            lane_obstacles[lane].append(float('inf'))

        curr_idx  = 0
        curr_lane = 2
        min_jumps = 0
        while curr_idx < len(obstacles) - 1:
            if obstacles[curr_idx + 1] != curr_lane:
                curr_idx += 1
            else:
                farest_fist_obstacle_idx  = curr_idx
                farest_fist_obstacle_lane = curr_lane

                for lane in [1, 2, 3]:
                    if lane == curr_lane:
                        continue
                    while len(lane_obstacles[lane]) > 0 and lane_obstacles[lane][0] <= curr_idx:
                        lane_obstacles[lane].popleft()
                    if len(lane_obstacles[lane]) > 0 and lane_obstacles[lane][0] > farest_fist_obstacle_idx and obstacles[curr_idx] != lane:
                        farest_fist_obstacle_idx  = lane_obstacles[lane][0]
                        farest_fist_obstacle_lane = lane
                if farest_fist_obstacle_lane == curr_lane:
                    for lane in [1, 2, 3]:
                        if lane != curr_lane:
                            curr_lane = lane
                            break
                else:
                    curr_lane = farest_fist_obstacle_lane

                min_jumps += 1
        
        return min_jumps

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-sideway-jumps/discuss/1152706/Python-Greedy-but-beats-100
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        obstacles += [0]
        curr_lane = 2
        min_jumps = 0

        curr_index = 0
        while curr_index < len(obstacles) - 1:
            if curr_lane == obstacles[curr_index + 1]:
                candidates = set([1, 2, 3])
                
                next_index = curr_index
                while len(candidates) > 1 and next_index < len(obstacles) - 1:
                    if obstacles[next_index] in candidates:
                        candidates.remove(obstacles[next_index])
                    next_index += 1
                
                curr_lane  = candidates.pop()
                curr_index = next_index - 1
                min_jumps += 1
            else:
                curr_index += 1

        return min_jumps
