# -----------------------------------------
# My Solution: Greedy
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# n := len(triplets)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_satisfied = [False] * 3
        for triplet in triplets:
            element_larger_than_target = False
            for index in (0, 1, 2):
                if triplet[index] > target[index]:
                    element_larger_than_target = True
                    break
            if element_larger_than_target:
                continue

            for index in (0, 1, 2):
                if triplet[index] == target[index]:
                    target_satisfied[index] = True
            if all(satisfied for satisfied in target_satisfied):
                return True

        return False
