# -----------------------------------------
# My Solution
# -----------------------------------------
# class Solution:
#     def combinationSum(self, candidates, target):
#         combinations = []
#
#         combination_dict = {}
#         def get_combination(current_combination, current_target):
#             if current_target == 0:
#                 current_combination.sort()
#                 combination_key = str(current_combination)
#
#                 if combination_dict.get(combination_key) is None:
#                     combination_dict[combination_key] = True
#                     combinations.append(current_combination)
#             elif current_target > 0:
#                 for candidate in candidates:
#                     if candidate <= current_target:
#                         get_combination(current_combination + [candidate], current_target - candidate)
#         for candidate in candidates:
#             if candidate <= target:
#                 get_combination([candidate], target - candidate)
#
#         return combinations

# -----------------------------------------
# Dynamic Programming
# -----------------------------------------
class Solution:
    def combinationSum(self, candidates, target):
        # NOTE: not use [[]] * N, it will generate N same list object. Ref: https://stackoverflow.com/a/33990699
        dp = [[] for _ in range(target + 1)]

        for candidate in candidates:
            for num in range(1, target + 1):
                if num == candidate:
                    dp[num].append([candidate])
                elif num > candidate:
                    for prev_list in dp[num - candidate]:
                        dp[num].append(prev_list + [candidate])

        return dp[target]

processor = Solution()
print(f"processor.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]:                  {processor.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]}")
print(f"processor.combinationSum([2, 3, 5], 8)    == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]: {processor.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]}")
print(f"processor.combinationSum([2], 1)          == []:                                {processor.combinationSum([2], 1) == []}")
print(f"processor.combinationSum([1], 1)          == [[1]]:                             {processor.combinationSum([1], 1) == [[1]]}")
