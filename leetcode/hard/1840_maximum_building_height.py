# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://leetcode.com/problems/maximum-building-height/discuss/1175142/JavaC%2B%2BPython-Two-Passes-Solution
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions) == 0:
            return n - 1

        restrictions += [[1, 0], [n, n - 1]]
        restrictions.sort()

        for index in range(len(restrictions) - 2, -1, -1):
            restrictions[index][1] = min(restrictions[index][1], restrictions[index + 1][1] + (restrictions[index + 1][0] - restrictions[index][0]))

        max_height = 0
        for index in range(1, len(restrictions)):
            restrictions[index][1] = min(restrictions[index][1], restrictions[index - 1][1] + (restrictions[index][0] - restrictions[index - 1][0]))
            # e.g. restrictions == [[2, 3], [12, 5]], distance between them is 12 - 2 == 10
            # add 3 to 5 first, take 2 buildings so 8 buildings left, so we got max height with 5 + 8 // 2 == 9. The heights of buildings list below
            # height:   3 4 5 6 7 8 9 8  7  6  5
            # position: 2 3 4 5 6 7 8 9 10 11 12
            height_to_add = ((restrictions[index][0] - restrictions[index - 1][0]) - abs(restrictions[index][1] - restrictions[index - 1][1])) // 2
            max_height = max(max_height, height_to_add + max(restrictions[index][1], restrictions[index - 1][1]))
        return max_height
