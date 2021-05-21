# -----------------------------------------
# My Solution
#
# Time  Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = sorted([a, b, c])
        # e.g. nums == [1, 3, 6]
        # for each move, we always choose one non-zero pile in [nums[0], nums[1]] and nums[2], like
        # [1, 3, 6] -> [0, 3, 5] -> [0, 2, 4] -> ... -> [0, 0, 2] => got score 4
        if nums[0] + nums[1] <= nums[2]:
            return nums[0] + nums[1]

        # e.g. nums == [375, 664, 1019]
        # 375 + 664 == 1039 -> 1039 - 1019 == 20
        # so for first 10 moves we always choose nums[0] and nums[1], then we can get nums[0] + nums[1] == nums[2] == 1019 (after first 10 moves)
        # one possible result after first 10 moves is [365, 654, 1019]
        # so we get score 10 + 1019 == 1029
        #
        # for another example nums == [3, 8, 8]
        # 3 + 8 == 11 -> 11 - 8 == 3
        # for first move we choose nums[0] and nums[1], then we can get nums[0] + nums[1] == 9 == nums[2] + 1 (after first move)
        # for same reason that max score of case nums[0] + nums[1] == nums[2] + 1 equals nums[0] + nums[1] since the final state would be (0, 0, 1)
        # so the max score is still num_diff // 2 + nums[2]
        num_diff = (nums[0] + nums[1]) - nums[2]
        return num_diff // 2 + nums[2]
