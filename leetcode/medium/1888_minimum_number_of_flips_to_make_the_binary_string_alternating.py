# -----------------------------------------
# Model Solution: Sliding Window
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/discuss/1253874/C%2B%2B-Solution-sliding-window.-O(N)
class Solution:
    def minFlips(self, s: str) -> int:
        # e.g. s == "110", so we have targets == ["010101", "101010"] and doubled == "110110"
        #      first for index == 2, we use targets[0][:3] == "010" and targets[1][:3] == "101" to check the number of flips
        #      and after index reaches 3 (in doubled), now we have targets[0][1:4] == "101" and targets[1][1:4] == "010"
        #      notice that what targets[0] and targets[1] represents changed, yet it doesn't matter because
        #
        #                                    current_index
        #                                           ↓
        #      doubled    == "1 1             0     1 1 0"
        #                       ↑             ↑
        #                prev_index_1  prev_index_2
        #                       ↓             ↓
        #      targets[0] == "0 1             0     1 0 1"
        #      targets[1] == "1 0             1     0 1 0"
        #
        #      we can see that the prev two bits comparision result still stored in target_0_flips and target_1_flips
        #      after add current flip (current bit same as targets[i][current_index] or not) and subtract previous flip (in this case is index 0)
        #      theb we get the correct flips needed for "101" and "010", doesn't matter it represents targets[0] or targets[1] now
        targets = ["01" * len(s), "10" * len(s)]
        doubled = s + s

        target_0_flips, target_1_flips, min_flips = 0, 0, float('inf')
        for index in range(len(doubled)):
            if doubled[index] != targets[0][index]:
                target_0_flips += 1
            if doubled[index] != targets[1][index]:
                target_1_flips += 1

            # the most left element is outside of sliding window, we need to subtract the diff if we do `flip`
            if index >= len(s):
                if doubled[index - len(s)] != targets[0][index - len(s)]:
                    target_0_flips -= 1
                if doubled[index - len(s)] != targets[1][index - len(s)]:
                    target_1_flips -= 1

            if index >= len(s) - 1:
                min_flips = min(min_flips, target_0_flips, target_1_flips)
        return min_flips
