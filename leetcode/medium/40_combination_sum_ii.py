# -----------------------------------------
# Model Solution: DFS + Pruning
#
# Time  Complexity: O(2^n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(candidates)
# Ref: https://leetcode.com/problems/top-k-frequent-elements/solution/
# Note: We can still pass all test data with pruning although time complexity is 2^n
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)[::-1]

        result = []
        def dfs(current_index, current_sum, path):
            if current_sum > target:
                return
            if current_sum == target:
                result.append(path)
                return

            for index in range(current_index, len(candidates)):
                if index > current_index and candidates[index] == candidates[index - 1]:
                    continue

                candidate = candidates[index]
                dfs(index + 1, current_sum + candidate, path + [candidate])

        dfs(0, 0, [])
        return result
