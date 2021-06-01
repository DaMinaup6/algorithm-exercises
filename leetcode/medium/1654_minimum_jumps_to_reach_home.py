# -----------------------------------------
# Model Solution: BFS
#
# Time  Complexity: O(a + b + x + m)
# Space Complexity: O(a + b + x + m)
# -----------------------------------------
# m := max(forbidden)
# Ref:
# a) https://www.youtube.com/watch?v=hn7k3udp2_8
# b) https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/937899/Python-BFS-with-double-queue-(80ms)/767506
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited_positions = {0}
        rightmost_position = a + b + x + max(forbidden) # ref: https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/937899/Python-BFS-with-double-queue-(80ms)/767506

        def position_valid(position):
            return position not in forbidden and position not in visited_positions and 0 < position < rightmost_position

        curr_positions = {0: ""}
        curr_jumps = 0
        while len(curr_positions) > 0:
            next_positions = {}
            for position in curr_positions.keys():
                visited_positions.add(position)
                if position == x:
                    return curr_jumps
                if position < rightmost_position and position_valid(position + a):
                    next_positions[position + a] = "forward"
                if curr_positions[position] != "backward" and position_valid(position - b) and position - b not in next_positions:
                    next_positions[position - b] = "backward"

            curr_positions = next_positions
            curr_jumps += 1
        return -1
