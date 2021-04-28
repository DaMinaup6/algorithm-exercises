# -----------------------------------------
# Model Solution: Boyer-Moore Voting Algorithm
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://zhuanlan.zhihu.com/p/352413242
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3

        candidates = [None, None]
        candidate_counts = [0, 0]
        for num in nums:
            if num == candidates[0]:
                candidate_counts[0] += 1
            elif num == candidates[1]:
                candidate_counts[1] += 1
            elif candidate_counts[0] == 0:
                candidates[0], candidate_counts[0] = num, 1
            elif candidate_counts[1] == 0:
                candidates[1], candidate_counts[1] = num, 1
            else:
                candidate_counts[0] -= 1
                candidate_counts[1] -= 1

        candidate_counts = [0, 0]
        for num in nums:
            for index in [0, 1]:
                if num == candidates[index]:
                    candidate_counts[index] += 1

        majority_elements = []
        if candidate_counts[0] > threshold:
            majority_elements.append(candidates[0])
        if candidate_counts[1] > threshold:
            majority_elements.append(candidates[1])
        return majority_elements
