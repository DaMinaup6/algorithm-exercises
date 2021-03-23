# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        accumulate_diff = [gas[0] - cost[0]]
        min_val = accumulate_diff[0]
        min_idx = 0
        # e.g. gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # calculate the accumulative diff, which would be [-2, -4, -6, -3, 0]
        # if we start from next position of the min accumulative diff, which is index 3, then we can get accumulative diff with [4, 2, 0, 3, 6]
        # no negative values there so it would be valid
        for index in range(1, len(gas)):
            accumulate_diff.append(gas[index] - cost[index] + accumulate_diff[index - 1])
            if accumulate_diff[index] <= min_val:
                min_val = accumulate_diff[index]
                min_idx = index
        
        return (min_idx + 1) % len(gas)

# -----------------------------------------
# Greedy
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://maxming0.github.io/2020/09/23/Gas-Station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx = 0
        curr_gas  = 0
        tot_gas   = 0
        for idx in range(len(gas)):
            diff = gas[idx] - cost[idx]
            tot_gas  += diff
            curr_gas += diff
            if curr_gas < 0:
                curr_gas  = 0
                start_idx = idx + 1

        return start_idx if tot_gas >= 0 else -1
