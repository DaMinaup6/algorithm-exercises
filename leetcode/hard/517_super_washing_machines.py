# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/qq_32805671/article/details/102610391
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        dresses_count = sum(machines)
        if dresses_count % len(machines) != 0:
            return -1

        target_dress_count = dresses_count // len(machines)
        minimum_move_count = 0
        curr_balance = 0
        for dress_count in machines:
            diff = dress_count - target_dress_count
            curr_balance += diff
            minimum_move_count = max(minimum_move_count, diff, abs(curr_balance))

        return minimum_move_count
