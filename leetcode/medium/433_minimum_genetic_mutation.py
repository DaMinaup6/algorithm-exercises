# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(bank)
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if len(bank) == 0:
            return -1
        bank_set = set(bank)
        if end not in bank_set:
            return -1

        min_mutation = float('inf')
        def dfs(curr_mutation, curr_mutation_count, available_mutations):
            nonlocal min_mutation

            if curr_mutation == end:
                min_mutation = min(min_mutation, curr_mutation_count)
                return

            for available_mutation in available_mutations:
                different_indexes = []
                for index in range(len(curr_mutation)):
                    if curr_mutation[index] != available_mutation[index]:
                        different_indexes.append(index)

                if len(different_indexes) == 1:
                    dfs(available_mutation, curr_mutation_count + 1, available_mutations - {curr_mutation, available_mutation})

        dfs(start, 0, bank_set)
        return min_mutation if min_mutation != float('inf') else -1
