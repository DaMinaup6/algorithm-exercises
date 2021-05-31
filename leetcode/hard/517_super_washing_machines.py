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

        # e.g. machines == [0, 0, 11, 5], so now our final number of dresses for each machine is 4
        #      so now we have requirement == [-4, -4, 7, 1] represents how many dresses we need (if genative) or
        #      need to send to other machines (if postive)
        #      for first machine (machines[0]), it requires 4 dresses and it can get from second machine (machines[1]), so now the
        #      requirement would be [0, -8, 7, 1]
        #      then we can get 7 dresses from third machine (machines[2]) but we need 8 dresses, so requirement == [0, 0, -1, 1]
        #      finally we get the last dress from last machine (machines[3]) and then requirement == [0, 0, 0, 0]
        #      the minimum number of moves during the process is 8 since we need to send 8 dresses to second machine
        target_dress_count = dresses_count // len(machines)
        minimum_move_count = 0
        curr_balance = 0
        for dress_count in machines:
            diff = dress_count - target_dress_count
            curr_balance += diff
            minimum_move_count = max(minimum_move_count, diff, abs(curr_balance))
        return minimum_move_count
